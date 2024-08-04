from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from mysite.utils.authentications import ApiTokenAuthentication, ApiPermission
from mysite.utils.paginations import GlobalPagination
from mysite.utils.decorators import swagger_auto_schema_with_paginator
from mysite.utils.serializers import stringifySerializereErrors
from mysite.utils.functions import md5
from mysite.utils.validators import validate_password
from ..models import User as UserModel
from rest_framework.exceptions import NotFound


# 以下个用于解决FBV在drf_yasg文档的显示
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

# 序列化器
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # 指定需要的字段
        fields = [
            "uid",
            "account",
            "nickname",
            "password",
            "group",
            "status",
            "create_datetime",
            "last_login_datetime",
        ]

    # 在返回数据时，动态去掉的字段
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # 从上下文中获取要移除的字段列表
        fields_to_remove = self.context.get("remove_fields", [])
        for field in fields_to_remove:
            representation.pop(field, None)
        return representation

# API实现
class UserManage(ViewSet, GenericAPIView):
    # 验证登录状态
    authentication_classes = [ApiTokenAuthentication]
    # 验证用户组权限
    permission_classes = [ApiPermission]
    # 设置用户组权限，[1，2]表示只允许group为1或2的用户组调用。如果不设置permission_groups则为全部允许。
    permission_groups = [1, 2]
    # 设置数据集
    queryset = UserModel.objects.all()
    # 设置序列化器
    serializer_class = UserSerializers
    # 设置分页器
    pagination_class = GlobalPagination
    # 查询主键
    lookup_field = "uid"

    # 获取单条用户记录
    def get_user(self):
        try:
            return self.get_object()
        except Http404:
            raise NotFound({"code": 404, "msg": "用户不存在", "data": {}})

    @swagger_auto_schema(
        tags=["用户管理"],
        operation_summary="新增用户",
    )
    def create(self, request):
        password = request.data.get("password")
        validate_password(password)
        # 因为 request.data不可修改，所以创建副本来修改password
        data = request.data.copy()
        data["password"] = md5(password)
        # 构建请求数据
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            # 数据校验成功，向数据库插入数据
            serializer.save()
            return Response(
                {
                    "code": 0,
                    "msg": "新增用户成功",
                    "data": {},
                }
            )
        else:
            # 数据校验失败，返回错误信息
            return Response(
                {
                    "code": 0,
                    "msg": stringifySerializereErrors(serializer.errors),
                }
            )

    @swagger_auto_schema_with_paginator(
        tags=["用户管理"],
        operation_summary="获取用户列表",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="用户昵称搜索",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
    )
    def list(self, request):
        # 获取分页器实例
        paginator = self.pagination_class()
        # 获取数据集
        user_list = self.get_queryset()
        # 获取搜索参数
        search = request.query_params.get("search")
        if search:
            # 过滤用户昵称中包含搜索词的用户
            user_list = user_list.filter(nickname__icontains=search)
        # 结合分页器查询的数据集
        result_list = paginator.paginate_queryset(user_list, request)
        # 构建序列化器对象，去除password字段
        serializer = self.get_serializer(
            result_list, many=True, context={"remove_fields": ["password"]}
        )
        # 使用分页器的响应方法返回分页数据
        return Response(
            {
                "code": 0,
                "msg": "成功",
                "data": {
                    "total": paginator.page.paginator.count,
                    "totalPage": paginator.page.paginator.num_pages,
                    "page": paginator.page.number,
                    "pageSize": paginator.get_page_size(request),
                    "list": serializer.data,
                },
            }
        )

    @swagger_auto_schema(
        tags=["用户管理"],
        operation_summary="获取单个用户信息",
    )
    def fetch(self, request, uid):
        user = self.get_user()
        serializer = self.get_serializer(
            instance=user, many=False, context={"remove_fields": ["password"]}
        )
        return Response({"code": 0, "msg": "成功", "data": serializer.data})

    @swagger_auto_schema(
        tags=["用户管理"],
        operation_summary="更新单个用户信息",
        operation_description="password为选填，不传则不修改密码。create_datetime和last_login_datetime不用传，传了也不会更新。",
    )
    def update(self, request, uid):
        user = self.get_user()
        password = request.data.get("password")
        # 因为 request.data不可修改，所以创建副本来修改password
        data = request.data.copy()
        # 删除不更新的字段（如果存在）
        data.pop("create_datetime", None)
        data.pop("last_login_datetime", None)
        if password is not None:
            validate_password(password)
            data["password"] = md5(password)
        # 如果不传password则取出并使用现存密码
        else:
            data["password"] = UserModel.objects.get(pk=uid).password

        serializer = self.get_serializer(
            instance=user, data=data, context={"remove_fields": ["password"]}
        )
        if serializer.is_valid():
            # 数据校验成功，向数据库更新数据
            serializer.save()
            return Response(
                {
                    "code": 0,
                    "msg": "更新成功",
                    "data": {},
                }
            )
        else:
            # 数据校验失败，返回错误信息
            return Response(
                {
                    "code": 400,
                    "msg": stringifySerializereErrors(serializer.errors),
                }
            )

    @swagger_auto_schema(
        tags=["用户管理"],
        operation_summary="删除单个用户",
    )
    def delete(self, request, uid):
        user = self.get_user()
        # request.user来自于登录状态验证类ApiTokenAuthentication返回的数据
        if uid == str(request.user.uid):
            return Response({"code": 401, "msg": "不能删除自己的账号", "data": {}})
        user.delete()
        return Response({"code": 0, "msg": "删除成功", "data": {}})

from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from mysite.utils.functions import md5
from mysite.settings import LOGIN_SALT, ACCESS_TOKEN_KEEPTIME
from ..models import User as UserModel
import secrets
from mysite.utils.authentications import ApiTokenAuthentication

class Signin(APIView):
    @swagger_auto_schema(
        tags=["个人账号"],
        operation_summary="用户登录",
        operation_description="如果原始password=123456，randmoCode=000000，则加密password=eff38392d709442340b2d65f9f1341db",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["account", "password", "randomCode"],
            properties={
                "account": openapi.Schema(
                    type=openapi.TYPE_STRING, description="登录账号"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="登录密码（前端加密后的）"
                ),
                "randomCode": openapi.Schema(
                    type=openapi.TYPE_STRING, description="随机码"
                ),
            },
        ),
    )
    def post(self, request):
        account = request.data.get("account")
        # 统一转换为小写字母，避免调用方MD5加密规范不统一
        password = request.data.get("password").lower()
        random_code = request.data.get("randomCode")

        if account is None:
            return Response({"code": 401, "msg": "未获取到账号", "data": {}})
        if password is None:
            return Response({"code": 401, "msg": "未获取到密码", "data": {}})
        if random_code is None:
            return Response({"code": 401, "msg": "未获取到随机码", "data": {}})
        # 查找用户记录
        user = UserModel.objects.filter(account=account).first()
        if user is None:
            return Response({"code": 401, "msg": "账号不存在"})
        if md5(user.password + LOGIN_SALT + random_code) != password:
            return Response({"code": 401, "msg": "密码不正确"})
        # 随机生成access_token
        user.access_token = secrets.token_urlsafe()
        # 设置access_token过期时间（天）
        user.access_token_expire = timezone.now() + timedelta(
            days=ACCESS_TOKEN_KEEPTIME
        )
        # 设置该用户最后登录时间（当前时间）
        user.last_login_datetime = timezone.now()
        # 更新数据库
        user.save()
        # 返回数据
        return Response(
            {
                "code": 0,
                "msg": "成功",
                "data": {
                    "uid": user.uid,
                    "nickname": user.nickname,
                    "accessToken": user.access_token,
                    "status": user.status,
                    "group": user.group,
                },
            }
        )
    
class Signout(APIView):
    # 验证登录状态
    authentication_classes = [ApiTokenAuthentication]

    @swagger_auto_schema(
        tags=["个人账号"],
        operation_summary="用户退出",
    )
    def post(self, request):
        user = UserModel.objects.get(pk=request.user.uid)
        user.access_token = None
        user.access_token_expire = None
        user.save()

        # 返回数据
        return Response(
            {
                "code": 0,
                "msg": "退出成功",
                "data": {},
            }
        )
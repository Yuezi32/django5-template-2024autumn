from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Article as ArticleModel
from rest_framework import serializers
from rest_framework.views import APIView
from mysite.utils.paginations import GlobalPagination
from mysite.utils.decorators import swagger_auto_schema_with_paginator
from mysite.utils.serializers import stringifySerializereErrors
from rest_framework.generics import GenericAPIView
from django.http import Http404
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ViewSet

# Create your views here.


# 【FBV演示】GET请求：通过URL query获取参数
@swagger_auto_schema(
    tags=["01：基于FBV的GET/POST请求"],
    method="get",
    operation_summary="通过URL?传参获取GET请求数据",
    manual_parameters=[
        openapi.Parameter(
            "q",
            openapi.IN_QUERY,
            description="查询参数q",
            type=openapi.TYPE_STRING,
            required=True,
        ),
        openapi.Parameter(
            "num",
            openapi.IN_QUERY,
            description="查询参数num",
            type=openapi.TYPE_INTEGER,
            required=True,
        ),
    ],
)
@api_view(["GET"])
def get_query(request):
    q = request.query_params.get("q")
    num = request.query_params.get("num")
    return Response(
        {
            "code": 0,
            "msg": "GET query:success",
            "data": {
                "q": q,
                "num": num,
            },
        }
    )


# 【FBV演示】GET请求：通过URL path获取参数
@swagger_auto_schema(
    tags=["01：基于FBV的GET/POST请求"],
    method="get",
    operation_summary="通过URL/path方式传参获取GET请求数据",
    manual_parameters=[
        openapi.Parameter(
            "q",
            openapi.IN_PATH,
            description="查询参数q",
            type=openapi.TYPE_STRING,
            required=True,
        ),
        openapi.Parameter(
            "num",
            openapi.IN_PATH,
            description="查询参数num",
            type=openapi.TYPE_INTEGER,
            required=True,
        ),
    ],
)
@api_view(["GET"])
def get_path(request, q, num):
    return Response(
        {
            "code": 0,
            "msg": "GET path:success",
            "data": {
                "q": q,
                "num": num,
            },
        }
    )


# 【FBV演示】POST请求：接收formdata数据
@swagger_auto_schema(
    tags=["01：基于FBV的GET/POST请求"],
    method="post",
    operation_summary="接收formdate格式的POST请求数据",
    manual_parameters=[
        openapi.Parameter(
            "q",
            openapi.IN_FORM,
            description="提交参数q",
            type=openapi.TYPE_STRING,
            required=True,
        ),
        openapi.Parameter(
            "num",
            openapi.IN_FORM,
            description="提交参数num",
            type=openapi.TYPE_INTEGER,
            required=True,
        ),
    ],
)
@api_view(["POST"])
@parser_classes([FormParser])
def post_formdate(request):
    q = request.data.get("q", "default")
    num = request.data.get("num")
    return Response(
        {
            "code": 0,
            "msg": "POST formdata:success",
            "data": {
                "q": q,
                "num": num,
            },
        }
    )


# 【FBV演示】POST请求：接收JSON数据
@swagger_auto_schema(
    tags=["01：基于FBV的GET/POST请求"],
    method="post",
    operation_summary="接收JSON格式的POST请求数据",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "q": openapi.Schema(type=openapi.TYPE_STRING, description="提交参数q"),
            "num": openapi.Schema(type=openapi.TYPE_INTEGER, description="提交参数num"),
        },
        required=["q", "num"],
    ),
)
@api_view(["POST"])
def post_json(request):
    q = request.data.get("q", "default")
    num = request.data.get("num")
    return Response(
        {
            "code": 0,
            "msg": "POST json:success",
            "data": {
                "q": q,
                "num": num,
            },
        }
    )


# CBV演示公用的模型序列化类
class ArticleSerializers(serializers.ModelSerializer):
    # 可以额外添加的自定义字段（以下相当于增加一个与author_uid字段值相同的author字段，区别在于author是非必填）
    # author = serializers.IntegerField(source="author_uid", required=False)
    # 格式化日期，并设为非必填
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        # 对接ArticleModel
        model = ArticleModel
        # 指定字段，也可以通过"__all__"指定所有字段
        # 例如：fields = "__all__"
        fields = ["id", "title", "content", "author_uid", "pub_date"]


class ArticleAPIView(APIView):
    # 新增文章
    @swagger_auto_schema(
        tags=["02：基于CBV的APIView类的请求"],
        operation_summary="新增文章",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            # 必填字段
            required=["title", "content", "author_uid"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章标题"
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章内容"
                ),
                "author_uid": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="作者UID"
                ),
            },
        ),
    )
    def post(self, request):
        # 构建请求数据
        serializer = ArticleSerializers(data=request.data)
        # 校验数据
        if serializer.is_valid():
            # 数据校验成功，向数据库插入数据
            # 符合格式的数据会存放在serializer.validated_data
            serializer.save()
            # API返回数据，serializer.data就是DRF序列化好的JSON数据
            return Response(
                {
                    "code": 0,
                    "msg": "新建成功",
                    # 返回新增记录的id值
                    "data": {"id": serializer.data.get("id")},
                }
            )
        else:
            # 不符合格式的数据会存放在serializer.errors，并附带错误原因
            # 数据校验失败，返回错误信息
            return Response(
                {
                    "code": 400,
                    "msg": stringifySerializereErrors(serializer.errors),
                }
            )

    # 查询文章列表
    @swagger_auto_schema_with_paginator(
        tags=["02：基于CBV的APIView类的请求"],
        operation_summary="查询文章列表",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="标题搜索",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
    )
    def get(self, request):
        # 实例化全局自定义分页器
        paginator = GlobalPagination()
        # 获取所有文章
        # Django 的查询集（QuerySet）是懒加载的，以下语句不会立即查询，而是结合分页器执行。
        article_list = ArticleModel.objects.all()
        # 获取搜索参数
        search = request.query_params.get("search")
        if search:
            # 过滤标题中包含搜索词的文章
            article_list = article_list.filter(title__icontains=search)
        # 结合分页器查询的数据集
        result_list = paginator.paginate_queryset(article_list, request)
        # 构建序列化器对象
        # 由于result_list是个数组，有多个元素，所以many=True
        serializer = ArticleSerializers(instance=result_list, many=True)
        # 使用DRF的Response，直接输出的JSON格式
        return Response(
            {
                "code": 0,
                "msg": "成功",
                "data": {
                    # 总条数
                    "total": paginator.page.paginator.count,
                    # 总页数
                    "totalPage": paginator.page.paginator.num_pages,
                    # 当前页码
                    "page": paginator.page.number,
                    # 每页条数
                    "pageSize": paginator.get_page_size(request),
                    "list": serializer.data,
                },
            }
        )


class ArticleOneAPIView(APIView):
    # 查询单条文章
    @swagger_auto_schema(
        tags=["02：基于CBV的APIView类的请求"],
        operation_summary="查询单条文章",
    )
    def get(self, request, id):
        try:
            article = ArticleModel.objects.get(pk=id)
        except ArticleModel.DoesNotExist:
            # 文章不存在
            return Response({"code": 404, "msg": "文章不存在", "data": {}})
        serializer = ArticleSerializers(instance=article, many=False)
        return Response({"code": 0, "msg": "成功", "data": serializer.data})

    # 更新单条文章
    @swagger_auto_schema(
        tags=["02：基于CBV的APIView类的请求"],
        operation_summary="更新单条文章",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "content", "author_uid"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章标题"
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章内容"
                ),
                "author_uid": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="作者UID"
                ),
            },
        ),
    )
    def put(self, request, id):
        try:
            update_article = ArticleModel.objects.get(pk=id)
        except ArticleModel.DoesNotExist:
            # 文章不存在
            return Response({"code": 404, "msg": "文章不存在", "data": {}})
        serializer = ArticleSerializers(instance=update_article, data=request.data)
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

    # 删除单条文章
    @swagger_auto_schema(
        tags=["02：基于CBV的APIView类的请求"],
        operation_summary="删除单条文章",
    )
    def delete(self, request, id):
        try:
            ArticleModel.objects.get(pk=id).delete()
        except ArticleModel.DoesNotExist:
            # 文章不存在
            return Response({"code": 404, "msg": "文章不存在", "data": {}})
        return Response({"code": 0, "msg": "删除成功", "data": {}})


class ArticleGenView(GenericAPIView):
    # queryset是GenericAPIView中定义好的属性，用于指定模型实例
    queryset = ArticleModel.objects.all()
    # serializer_class是GenericAPIView中定义好的属性，用于指定序列化器
    serializer_class = ArticleSerializers
    # pagination_class是GenericAPIView中定义好的属性，用于指定分页器
    pagination_class = GlobalPagination

    # 新增文章
    @swagger_auto_schema(
        tags=["03：基于CBV的GenericAPIView类的请求"],
        operation_summary="新增文章",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            # 必填字段
            required=["title", "content", "author_uid"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章标题"
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章内容"
                ),
                "author_uid": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="作者UID"
                ),
            },
        ),
    )
    def post(self, request):
        # 构建序列化器对象
        serializer = self.get_serializer(data=request.data)
        # 校验数据
        if serializer.is_valid():
            # 数据校验成功，向数据库插入数据
            # 符合格式的数据会存放在serializer.validated_data
            serializer.save()
            return Response(
                {
                    "code": 0,
                    "msg": "新建成功",
                    "data": {"id": serializer.data.get("id")},
                }
            )
        else:
            # 不符合格式的数据会存放在serializer.errors，并附带错误原因
            # 数据校验失败，返回错误信息
            return Response(
                {
                    "code": 400,
                    "msg": stringifySerializereErrors(serializer.errors),
                }
            )

    # 查询文章列表
    @swagger_auto_schema_with_paginator(
        tags=["03：基于CBV的GenericAPIView类的请求"],
        operation_summary="查询文章列表",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="标题搜索",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
    )
    def get(self, request):
        # 获取分页器实例
        paginator = self.pagination_class()
        # 获取数据集
        article_list = self.get_queryset()
        # 获取搜索参数
        search = request.query_params.get("search")
        if search:
            # 过滤标题中包含搜索词的文章
            article_list = article_list.filter(title__icontains=search)
        # 结合分页器查询的数据集
        result_list = paginator.paginate_queryset(article_list, request)
        # 构建序列化器对象
        serializer = self.get_serializer(result_list, many=True)
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


class ArticleOneGenView(GenericAPIView):

    # queryset是GenericAPIView中定义好的属性，用于指定模型实例
    queryset = ArticleModel.objects.all()
    # serializer_class是GenericAPIView中定义好的属性，用于指定序列化器
    serializer_class = ArticleSerializers
    # 用于指定单条记录的字段，默认情况下，这个字段是"pk"，即模型实例的主键（通常是id字段）
    lookup_field = "id"

    # 获取单条文章记录
    def get_article(self):
        try:
            return self.get_object()
        except Http404:
            raise NotFound({"code": 404, "msg": "文章不存在", "data": {}})

    # 查询单条文章
    @swagger_auto_schema(
        tags=["03：基于CBV的GenericAPIView类的请求"],
        operation_summary="查询单条文章",
    )
    def get(self, request, id):
        article = self.get_article()
        serializer = self.get_serializer(instance=article, many=False)
        return Response({"code": 0, "msg": "成功", "data": serializer.data})

    # 更新单条文章
    @swagger_auto_schema(
        tags=["03：基于CBV的GenericAPIView类的请求"],
        operation_summary="更新单条文章",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "content", "author_uid"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章标题"
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章内容"
                ),
                "author_uid": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="作者UID"
                ),
            },
        ),
    )
    def put(self, request, id):
        article = self.get_article()
        serializer = self.get_serializer(instance=article, data=request.data)
        if serializer.is_valid():
            # 数据校验成功，向数据库更新数据
            ## 使用serializer更新数据
            serializer.save()
            return Response(
                {
                    "code": 0,
                    "msg": "更新成功",
                    "data": {"id": serializer.data.get("id")},
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

    # 删除单条文章
    @swagger_auto_schema(
        tags=["03：基于CBV的GenericAPIView类的请求"],
        operation_summary="删除单条文章",
    )
    def delete(self, request, id):
        article = self.get_article()
        article.delete()
        return Response({"code": 0, "msg": "删除成功", "data": {}})


class ArticleViewSet(ViewSet, GenericAPIView):
    # queryset是GenericAPIView中定义好的属性，用于指定模型实例
    queryset = ArticleModel.objects.all()
    # serializer_class是GenericAPIView中定义好的属性，用于指定序列化器
    serializer_class = ArticleSerializers
    # pagination_class是GenericAPIView中定义好的属性，用于指定分页器
    pagination_class = GlobalPagination
    # 用于指定单条记录的字段，默认情况下，这个字段是"pk"，即模型实例的主键（通常是id字段）
    lookup_field = "id"

    # 获取单条文章记录
    def get_article(self):
        try:
            return self.get_object()
        except Http404:
            raise NotFound({"code": 404, "msg": "文章不存在", "data": {}})

    # 新增文章
    @swagger_auto_schema(
        tags=["04：基于CBV的ViewSet类的请求"],
        operation_summary="新增文章",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            # 必填字段
            required=["title", "content", "author_uid"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章标题"
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章内容"
                ),
                "author_uid": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="作者UID"
                ),
            },
        ),
    )
    def create(self, request):
        # 构建序列化器对象
        serializer = self.get_serializer(data=request.data)
        # 校验数据
        if serializer.is_valid():
            # 数据校验成功，向数据库插入数据
            # 符合格式的数据会存放在serializer.validated_data
            serializer.save()
            return Response(
                {
                    "code": 0,
                    "msg": "新建成功",
                    "data": {"id": serializer.data.get("id")},
                }
            )
        else:
            # 不符合格式的数据会存放在serializer.errors，并附带错误原因
            # 数据校验失败，返回错误信息
            return Response(
                {
                    "code": 400,
                    "msg": stringifySerializereErrors(serializer.errors),
                }
            )

    # 查询文章列表
    @swagger_auto_schema_with_paginator(
        tags=["04：基于CBV的ViewSet类的请求"],
        operation_summary="查询文章列表",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="标题搜索",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ],
    )
    def list(self, request):
        # 获取分页器实例
        paginator = self.pagination_class()
        # 获取数据集
        article_list = self.get_queryset()
        # 获取搜索参数
        search = request.query_params.get("search")
        if search:
            # 过滤标题中包含搜索词的文章
            article_list = article_list.filter(title__icontains=search)
        # 结合分页器查询的数据集
        result_list = paginator.paginate_queryset(article_list, request)
        # 构建序列化器对象
        serializer = self.get_serializer(result_list, many=True)
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

    # 查询单条文章
    @swagger_auto_schema(
        tags=["04：基于CBV的ViewSet类的请求"],
        operation_summary="查询单条文章",
    )
    def fetch(self, request, id):
        article = self.get_article()
        serializer = self.get_serializer(instance=article, many=False)
        return Response({"code": 0, "msg": "成功", "data": serializer.data})

    # 更新单条文章
    @swagger_auto_schema(
        tags=["04：基于CBV的ViewSet类的请求"],
        operation_summary="更新单条文章",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "content", "author_uid"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章标题"
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING, description="文章内容"
                ),
                "author_uid": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="作者UID"
                ),
            },
        ),
    )
    def update(self, request, id):
        article = self.get_article()
        serializer = self.get_serializer(instance=article, data=request.data)
        if serializer.is_valid():
            # 数据校验成功，向数据库更新数据
            ## 使用serializer更新数据
            serializer.save()
            return Response(
                {
                    "code": 0,
                    "msg": "更新成功",
                    "data": {"id": serializer.data.get("id")},
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

    # 删除单条文章
    @swagger_auto_schema(
        tags=["04：基于CBV的ViewSet类的请求"],
        operation_summary="删除单条文章",
    )
    def delete(self, request, id):
        article = self.get_article()
        article.delete()
        return Response({"code": 0, "msg": "删除成功", "data": {}})

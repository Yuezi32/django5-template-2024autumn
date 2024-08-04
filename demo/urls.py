from django.urls import path
# 从当前目录导入views.py模块
from . import views

# 加载路由
urlpatterns = [
    # 基于FBV的GET请求：query方式传参
    path("get_fbv/", views.get_query),
    # 基于FBV的GET请求：path方式传参
    path("get_fbv/<str:q>/<int:num>", views.get_path),
    # 基于FBV的POST请求：接收formdata数据
    path("post_fbv_formdata/", views.post_formdate),
    # 基于FBV的POST请求：接收JSON数据
    path("post_fbv_json/", views.post_json),
    # 基于CBV的APIView类的请求
    path("apiview/article/", views.ArticleAPIView.as_view()),
    path("apiview/article/<id>", views.ArticleOneAPIView.as_view()),
    # 基于CBV的GenericAPIView类的请求
    path("genericview/article/", views.ArticleGenView.as_view()),
    path("genericview/article/<id>", views.ArticleOneGenView.as_view()),
    # 基于CBV的ViewSet+GenericAPIView类的请求
    path(
        "viewset/article/",
        views.ArticleViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "viewset/article/<id>",
        views.ArticleViewSet.as_view(
            {"get": "fetch", "put": "update", "delete": "delete"}
        ),
    ),
]
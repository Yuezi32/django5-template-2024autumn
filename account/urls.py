from django.urls import path
from .views import privateViews, userManageViews

# 加载路由
urlpatterns = [
    path("signin/", privateViews.Signin.as_view()),
    path("signout/", privateViews.Signout.as_view()),
    path("user/", userManageViews.UserManage.as_view({
        "get": "list",
        "post": "create"
    })),
    path("user/<uid>", userManageViews.UserManage.as_view({
        "get": "fetch",
        "put": "update",
        "delete": "delete"
    })),
]
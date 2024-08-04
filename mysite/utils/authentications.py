from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from account.models import User as UserModel
from django.utils import timezone


# 验证登录状态
class ApiTokenAuthentication(TokenAuthentication):
    # 构建用于返回登录用户信息的类
    class AUTH_USER:
        def __init__(
            self, uid: int, account: str, status: int, nickname: str, group: str
        ):
            self.uid = uid
            self.account = account
            self.status = status
            self.nickname = nickname
            self.group = group

    def authenticate(self, request):
        # 从请求头中获取Login-Uid
        uid = request.headers.get("Login-Uid")
        # 从请求头中获取Access-token
        access_token = request.headers.get("Access-token")
        if uid is None or access_token is None:
            raise NotAuthenticated({"msg": "未获取到登录授权信息"})
        try:
            # 通过uid从数据库中找到用户记录
            user_info = UserModel.objects.get(pk=uid)
        except UserModel.DoesNotExist:
            raise NotAuthenticated({"msg": "账号不存在"})
        # 数据库中access_token为空，或者access_token不正确
        if (
            user_info.access_token is None
            or user_info.access_token == ""
            or user_info.access_token != access_token
        ):
            raise AuthenticationFailed({"msg": "登录状态已失效"})
        if user_info.status == 0:
            raise AuthenticationFailed("该账号已冻结")
        if (
            user_info.access_token_expire is None
            or timezone.now() >= user_info.access_token_expire
        ):
            raise AuthenticationFailed({"msg": "登录状态已过期"})

        # 实例化用户信息对象
        user = self.AUTH_USER(
            uid=user_info.uid,
            account=user_info.account,
            status=user_info.status,
            nickname=user_info.nickname,
            group=user_info.group,
        )
        # 这里返回的用户信息放在request.user中
        return (user, None)


# 验证用户权限
class ApiPermission(BasePermission):
    def has_permission(self, request, view):
        # 获取在view上定义的permission_groups，permission_groups表示拥有此权限的用户组
        permission_groups = getattr(view, "permission_groups", None)
        # 如果“授权用户组为空”或者“用户存在于授权的用户组”，则表示权限验证通过
        if permission_groups is None or request.user.group in permission_groups:
            return True
        # 否则，权限验证不通过
        return False

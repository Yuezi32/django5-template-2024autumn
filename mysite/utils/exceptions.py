from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    ValidationError,
    PermissionDenied,
    NotAuthenticated,
    ParseError,
    NotFound,
    AuthenticationFailed,
)
from django.http import Http404


# 全局通用异常处理
def global_exception_handler(exc, context):

    # 调用DRF的默认异常处理函数获取标准错误响应
    response = exception_handler(exc, context)

    # 初始化默认的自定义错误响应
    custom_response_data = {
        "code": -1,  # -1表示未知错误代号
        "msg": "服务器错误",
        "data": {},
    }

    # 如果DRF捕获了异常
    if response is not None:
        # 根据异常类型，提供更具体的错误信息
        if isinstance(exc, ValueError):
            custom_response_data["code"] = 400
            custom_response_data["msg"] = "输入参数错误"
        elif isinstance(exc, NotFound):
            custom_response_data["code"] = 404
            custom_response_data["msg"] = "资源不存在"
        elif isinstance(exc, ValidationError):
            custom_response_data["code"] = 400
            custom_response_data["msg"] = "验证错误"
        elif isinstance(exc, PermissionDenied):
            custom_response_data["code"] = 403
            custom_response_data["msg"] = "权限不足"
        elif isinstance(exc, NotAuthenticated):
            custom_response_data["code"] = 401
            custom_response_data["msg"] = "未授权的访问"
        elif isinstance(exc, ParseError):
            custom_response_data["code"] = 400
            custom_response_data["msg"] = "解析错误"
        elif isinstance(exc, AuthenticationFailed):
            custom_response_data["code"] = 401
            custom_response_data["msg"] = "授权验证失败"
        elif isinstance(exc, Http404):
            custom_response_data["code"] = 404
            custom_response_data["msg"] = "访问的资源不存在"
        # 如果传递了异常信息，并且是字典，则覆盖默认的自定义错误响应
        if isinstance(getattr(exc, "detail", None), dict):
            custom_response_data.update(exc.detail)
        response.data = custom_response_data
        return response
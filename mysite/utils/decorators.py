from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 用于swagger补充显示分页器参数的通用装饰器
def swagger_auto_schema_with_paginator(*args, **kwargs):
    # 定义默认的 manual_parameters
    default_params = [
        openapi.Parameter(
            name="page",
            in_=openapi.IN_QUERY,
            description="页码",
            default="1",
            type=openapi.TYPE_INTEGER,
        ),
        openapi.Parameter(
            name="pageSize",
            in_=openapi.IN_QUERY,
            default="10",
            type=openapi.TYPE_INTEGER,
            description="每页条数",
        ),
    ]

    # 获取用户可能传递的 manual_parameters
    manual_params = kwargs.get("manual_parameters", [])

    # 合并参数列表，同时确保不重复
    seen_keys = set()
    final_params = []
    for param in manual_params + default_params:
        if param.name not in seen_keys:
            final_params.append(param)
            seen_keys.add(param.name)

    # 更新kwargs的manual_parameters为合并后的结果
    kwargs["manual_parameters"] = final_params

    # 返回应用了原始swagger_auto_schema装饰器的新函数
    return swagger_auto_schema(*args, **kwargs)
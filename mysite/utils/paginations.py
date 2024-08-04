from rest_framework.pagination import PageNumberPagination

# 通用分页器
class GlobalPagination(PageNumberPagination):
    # 页码的请求接收参数名，默认为page
    page_query_param = "page"
    # 每页条数的请求接收参数名，默认为None
    page_size_query_param = "pageSize"
    # 最大pageSize，默认为None
    max_page_size = 100
    # 默认pageSize，默认为None
    page_size = 10
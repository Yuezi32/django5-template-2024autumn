from django.contrib import admin
from .models import Article
from django.utils.dateformat import format

# Register your models here.

# 用于控制在Django管理后台的数据表显示哪些
class ArticleDjangoAdmin(admin.ModelAdmin):
    # 自定义一个新的字段
    def formatted_pub_date(self, obj):
        # 将pub_date字段进行格式化
        return format(obj.pub_date, 'Y-m-d H:i:s')
    # 允许formatted_pub_date按pub_date字段进行排序
    formatted_pub_date.admin_order_field = 'pub_date'
    # 设置formatted_pub_date在管理后台中显示的标题
    formatted_pub_date.short_description = '发布时间'
    # 设置在Django管理后台显示的字段
    list_display = ('title', 'content', 'author_uid', 'formatted_pub_date')

admin.site.register(Article, ArticleDjangoAdmin)
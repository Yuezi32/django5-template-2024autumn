from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    # 如果不指定自增主键字段，默认会自动生成字段名为id的自增主键字段。
    # verbose_name，表示字段名称
    # max_length，表示最大长度
    # default， 表示默认值
    # null=True，表示允许为空
    # unique=True，表示字段值唯一
    title = models.CharField(max_length=50, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    author_uid = models.IntegerField(verbose_name="作者uid")
    pub_date = models.DateTimeField(verbose_name="发布时间", default=timezone.now)
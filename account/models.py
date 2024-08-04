from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    # 如果唯一，则添加unique=True
    # 如果允许为空，则添加null=True（针对数据库表结构设定）
    # 如果允许提交表单时不填写该字段，blank=True（针对Django管理后台的表单验证）
    # 如果设置默认值，则添加default=xxx
    uid = models.AutoField(primary_key=True, auto_created=True)
    account = models.CharField(max_length=50, verbose_name="登录账号", unique=True)
    password = models.CharField(max_length=100, verbose_name="登录密码")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    group = models.SmallIntegerField(verbose_name="分组", default=2,  help_text="1=超级管理员；2=管理员；3=普通用户")
    status = models.SmallIntegerField(verbose_name="状态", default=1, help_text="0=冻结；1=正常；")
    create_datetime = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    last_login_datetime = models.DateTimeField(verbose_name="最后登录时间", null=True, default=None, blank=True)
    access_token=models.CharField(max_length=50, verbose_name="登录验证Token", null=True, default=None, blank=True)
    access_token_expire = models.DateTimeField(verbose_name="登录Token过期时间", null=True, default=None, blank=True)
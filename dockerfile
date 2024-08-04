# 拉取Dockerhub官方Python镜像
FROM python:3.12.4

# 创建项目目录
RUN mkdir /home/django-server
# 创建项目日志目录
RUN mkdir /home/django-server/log
# 复制需要的项目文件到镜像中
COPY ./account /home/django-server/account
COPY ./demo /home/django-server/demo
COPY ./mysite /home/django-server/mysite
COPY ./manage.py /home/django-server
COPY ./requirements.txt /home/django-server

# 进入项目目录
WORKDIR /home/django-server

# 安装项目依赖包
RUN pip install -r requirements.txt

# 启动开发环境服务
# CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
# 启动正式环境服务
CMD ["uvicorn", "mysite.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
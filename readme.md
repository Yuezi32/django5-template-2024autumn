# 2024金秋版：Django5开发与部署保姆级零基础教程

精心整理的适合初学者的Django速成教程。把知识点与实操相结合，把晦涩的概念变得通俗易懂。

手把手带你快速扎实基础、掌握实战，开发+部署，快速晋级Django架构师。节约大量自己学习、摸索、爬坑的时间。


## 配套教程

📚📚本项目有详细的讲解教程，原文请关注我的微信公众号【卧梅又闻花】📚📚

[《2024金秋版：Django5开发与部署保姆级零基础教程（上篇）》](https://mp.weixin.qq.com/s/fiYFT4ALxZWYIcquQpzI5w)

[《2024金秋版：Django5开发与部署保姆级零基础教程（下篇）》](https://mp.weixin.qq.com/s/fiYFT4ALxZWYIcquQpzI5w)

先看下目录了解本教程都有哪些内容。

## 章节目录
```
1 搭建Python环境
• 1.1 Windows安装Python
• 1.2 Windows切换系统全局Python版本
• 1.3 macOS安装Python
• 1.4 macOS使用pyenv切换系统默认Python版本
• 1.5 为什么要构建Python虚拟环境
• 1.6 使用Python自带工具构建Python虚拟环境
• 1.7 退出虚拟环境
2 初始化Django项目
• 2.1 创建项目虚拟环境
• 2.2 设置VSCode自动激活虚拟环境
• 2.3 修改pip镜像源
• 2.4 创建Django项目代码
• 2.5 初次启动Django项目
• 2.6 导出项目依赖包
• 2.7 路由小试：替换Django默认欢迎页
• 2.8 Debug模式开启与关闭
• 2.9 设置项目时区
• 2.10 设置项目环境变量文件.env
• 2.11 建议的.gitignore文件配置
3 Demo应用教学：基于FBV的API开发
• 3.1 FBV和CBV
• 3.2 创建Demo应用
• 3.3 基于FBV开发API：GET请求
• 3.3.1 GET请求：query方式传参
• 3.3.2 使用Django的JsonResponse返回JSON数据
• 3.3.3 GET请求：path方式传参
• 3.4 基于FBV开发API：POST请求
• 3.4.1 POST请求：接收formdata数据
• 3.4.2 关闭跨站请求伪造（CSRF）保护
• 3.4.3 POST请求：接收JSON数据
4 Django REST framework（DRF）
• 4.1 什么是Django REST framework
• 4.2 安装Django REST framework
• 4.3 使用api_view装饰器解决跨站请求伪造（CSRF）保护
• 4.4 使用DRF简化FBV的API代码
• 4.5 解决浏览器无法直接访问DRF的GET请求地址的问题
5 使用Swagger自动生成API文档
• 5.1 安装drf-yasg
• 5.2 Swagger UI与ReDoc
• 5.3 继续完善API文档的说明
• 5.4 在Swagger页面中调试API
6 Demo应用教学：基于CBV的API开发
• 6.1 开发需求
• 6.2 创建数据库模型（Model）
• 6.3 使用Django自带的SQLite数据库
• 6.4 使用makemigrations和migrate创建数据库表结构
• 6.5 makemigrations指令和migrate指令的区别
• 6.6 构建数据库模型序列化器（ModelSerializer）
• 6.7 基于APIView类的实现方式
• 6.7.1 实现新增文章API
• 6.7.2 实现查询文章列表API（含搜索）
• 6.7.3 构建公共工具库：分页器
• 6.7.4 构建公共工具库：Swagger分页查询装饰器
• 6.7.5 构建公共工具库：全局异常处理
• 6.7.6 构建公共工具库：序列化器相关处理
• 6.7.7 实现查询指定文章API
• 6.7.8 实现更新指定文章API
• 6.7.9 实现删除指定文章API
• 6.8 基于GenericAPIView类的实现方式
• 6.8.1 实现新增文章和查询文章列表API
• 6.8.2 实现对指定文章的查询、更新、删除API
• 6.9 基于ViewSet类的实现方式
• 6.10 其他更高封装度的混合类（选读）   
7 Django自带的Admin管理后台
• 7.1 创建管理员账号
• 7.2 加入自建应用Article数据表
• 7.3 定制Article数据表的字段显示
8 实战应用教学：开发用户管理系统
• 8.1 项目需求
• 8.2 创建Account应用和用户（User）表
• 8.3 实现用户登录API
• 8.4 构建公共工具库：API登录状态及权限验证
• 8.5 实现用户退出API
• 8.6 在Swagger页面携带所需的请求头数据
• 8.7 构建公共工具：数据合法验证器
• 8.8 实现用户“增删改查查”5个API
9 迁移至MySQL数据库
• 9.1 安装mysqlclient
• 9.2 设置Django数据库驱动配置
• 9.3 导出SQLite中的全部数据
• 9.4 执行迁移MySQ数据库
10 将运行日志写入文件
• 10.1 日志保存的规则、格式和内容
• 10.2 构建公共工具库：日志文件处理
• 10.3 配置Django日志
• 10.4 关于runserver与uvicorn生成日志的区别
11 部署生产环境
• 11.1 安装并运行uvicorn
• 11.2 关于生产环境加载静态资源的问题
• 11.3 使用Docker部署
• 11.3.1 创建项目专用Network
• 11.3.2 编写Django项目的dockerfile
• 11.3.3 编写Nginx配置和dockerfile
• 11.3.4 编写Nginx+Django+MySQL的docker compose文件
• 11.3.5 使用docker compose一键启动整体项目
• 11.3.6 相关的其他docker compose命令
• 11.3.7 Docker学习推荐阅读
• 11.3.8 关于生产环境部署的安全考虑因素
• 11.3.9 检查项目依赖包是否有更新
• 11.4 最终项目目录结构
12 教程Git源码
结束语
```

## 教程使用的系统环境及软件版本
```
【操作系统】
Windows 11
macOS Sonoma 14

【Docker软件】
Docker Engine: 27.1.1
Docker Desktop: 4.33.0
Docker Compose: v2.29.1-desktop.1

【Docker镜像】
mysql: 8.4.2
nginx: 1.27.0
python: 3.12.4

【主要Python依赖包】
Django: 5.0.7
django-environ 0.11.2
djangorestframework: 3.15.2
drf-yasg: 1.21.7
mysqlclient: 2.2.4
uvicorn 0.30.3
```

## 目录结构说明
```
├─ /django5-template-2024autumn
|  ├─ /_sql						<-- 教程配套数据库文件临时目录
|  |  └─ my_django.sql			<-- 方便导入MySQL的教程配套数据库文件目录
|  ├─ /.vscode					<-- VSCode配置目录
|  ├─ /account		   	   		<-- account应用目录
|  ├─ /demo						<-- demo应用目录
|  ├─ /log		   				<-- 日志目录
|  ├─ /mysite		   			<-- 项目程序包目录
|  |  ├─ __init__.py  			<-- 一个空文件，这种文件名用于将目录识别为一个Python包
|  |  ├─ asgi.py   	   			<-- 项目运行在ASGI兼容的Web服务器上的入口
|  |  ├─ settings.py   			<-- Django项目配置文件
|  |  ├─ urls.py   	   			<-- Django项目的路由配置文件
|  |  └─ wsgi.py   	   			<-- 项目运行在WSGI兼容的Web服务器上的入口
|  ├─ /nginx		   			<-- 项目程序包目录
|  |  ├─ default.conf			<-- Nginx配置文件
|  |  └─ dockerfile				<-- Nginx服务容器的dockerfile
|  ├─ /venv			   			<-- Python虚拟环境集合目录
|  ├─ .env			   			<-- 项目环境变量文件
|  ├─ .gitignore				<-- git忽略配置文件
|  ├─ compose-production.yaml	<-- 整体项目一键部署docker compose文件
|  ├─ data.json					<-- 导出的sqlite教材配套数据文件，用于migrate至mysql
|  ├─ db.sqlite3				<-- 教程配套的临时SQLite数据库文件
|  ├─ dockerfile				<-- Django API项目的dockerfile文件
|  ├─ manage.py		   			<-- Django命令行管理工具
|  └─ requirements.txt			<-- Django项目依赖包
```

## 使用说明

### 创建并激活虚拟环境
进入项目根目录执行：
```
cd venv
python -m venv venv-3.12.4
```

```venv-3.12.4```是虚拟环境目录的名称，可以随意命名。这里表示根据当前系统环境的Python 3.12.4创建虚拟环境。

在项目根目录，执行：
```
# Windows系统
venv\venv-3.12.4\Scripts\activate

# macOS系统
source venv/venv-3.12.4/bin/activate
```

### 安装项目依赖包
在项目根目录，执行：
```
pip install -r requirements.txt
```

### 启动开发环境服务
在项目根目录，执行：
```
python manage.py runserver
```

### 启动生产环境服务
```
uvicorn mysite.asgi:application --host 0.0.0.0 --port 8000
```
> 生产环境使用的是mysql数据库，不建议切换为sqlite，并且dockerfile中也没有导入db.sqlite文件。

### 部署Docker
#### 创建项目专用Network

创建项目自定义Network，驱动模式为bridge，执行：
```
docker network create -d bridge docker-django
```
本综合实战案例统一使用docker-django作为项目专用网络。

#### 修改docker-django-mysql和docker-django-api容器的挂载目录
请根据实际需要，修改以下目录：
```
services:
    # MySQL服务
    mysql:
        ...（略）
        # 请修改这里的目录
        volumes: 
        - D:/docker-django/mysql:/var/lib/mysql
        ...（略）
    # Django API服务
    django-server:
        ...（略）
        # 请修改这里的目录
        volumes: 
        - D:/docker-django/log:/home/django-server/log
        ...（略）
```
#### 执行docker compose
```
docker compose -f ./compose-production.yaml up -d
```
> docker-django-mysql容器3306端口已映射到宿主机3306端口
> 
> docker-django-nginx容器80端口已映射到宿主机80端口
>
> 请确保宿主机端口没有被占用，如需调整端口可修改compose-production.yaml

## 初始化自带的账号
### Django管理后台账号
地址：
```
http://localhost:8000/admin/
Username: admin
Password: 123456
```
### 业务用户系统
```
acount: test_user
randmoCode: 000000
password: eff38392d709442340b2d65f9f1341db
```
> 注：以上password为加密后的密码，原始密码为123456

## 其他说明
### 开发环境切换sqlite和MySQL数据库
修改.env文件：
```
# 数据库类型(可选值：mysql或sqlite)
DB_TYPE=sqlite
```
### 生产环境数据库配置
修改compose-production.yaml：
```
...（略）
environment: 
    # 是否开启DEBUG模式
    - DEBUG=False
    # 数据库类型(可选值：mysql或sqlite)
    - DB_TYPE=sqlite
    # MYSQL主机地址（处于同一个Docker Network内，可直接填写容器名称）
    - DB_MYSQL_HOST=docker-django-mysql
    # MYSQL数据库名称
    - DB_MYSQL_NAME=my_django
    # MYSQL账号
    - DB_MYSQL_USER=root
    # MYSQL密码
    - DB_MYSQL_PASSWORD=12345678
    # MYSQL端口
    - DB_MYSQL_PORT=3306
```

### 其他会使用到的命令
#### 导出依赖包
```
pip freeze > requirements.txt
```

#### 迁移数据库
```
python manage.py makemigrations
python manage.py migrate   
```

#### 导出SQLite中的全部数据
```
python manage.py dumpdata > data.json
```

#### 导入json格式的数据库文件
```
python manage.py loaddata data.json
```

💖 得“鱼🐟”，不如会“渔🎣”，原文请关注我的微信公众号【卧梅又闻花】💖

[《2024金秋版：Django5开发与部署保姆级零基础教程（上篇）》](https://mp.weixin.qq.com/s/fiYFT4ALxZWYIcquQpzI5w)

[《2024金秋版：Django5开发与部署保姆级零基础教程（下篇）》](https://mp.weixin.qq.com/s/fiYFT4ALxZWYIcquQpzI5w)


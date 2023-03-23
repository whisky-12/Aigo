# []()algorithm-engine

[![img](https://img.shields.io/badge/python-%3E=3.7.x-green.svg)](https://python.org/)  [![PyPI - Django Version badge](https://img.shields.io/badge/django%20versions-3.2-blue)](https://docs.djangoproject.com/zh-hans/3.2/) 


💡 **「关于」**

这是使用 **django-rest-framework** 封装的算法引擎，通过API暴露算法函数。


## 前置知识

👩‍👦‍👦文档地址：[https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

## 准备工作
```
Python >= 3.8.0 (推荐3.8+版本)
```

## 引擎💈

```bash
1. 进入项目根目录
2. 在项目根目录中，复制 ./conf/env.example.py 文件为一份新的到 ./conf 文件夹下，并重命名为 env.py
3. 在 env.py 中无需改动（暂时）
4. 安装依赖环境
	pip3 install -r requirements.txt
5. 执行迁移命令：
	python manage.py makemigrations
	python manage.py migrate
6. 初始化数据
	python manage.py init
7. 启动项目
	python manage.py runserver 0.0.0.0:8000
或使用 daphne :
  daphne -b 0.0.0.0 -p 8000 application.asgi:application
```

### 访问API

- 访问地址：[http://localhost:8000](http://localhost:8000) (默认为此地址，如有修改请按照配置文件)


### docker 镜像打包

#### 打包基础Build包

~~~sh
# 编译打包到本地
docker build -f ./DockerfileBuild -t harbor.flydiysz.cn:8888/flydiy-base/python38-base-algorithm-engine:latest .
# 上传到Docker Hub
docker push harbor.flydiysz.cn:8888/flydiy-base/python38-base-algorithm-engine:latest
~~~

# docker 镜像打包

### 打包基础Build包

~~~sh
# 编译打包到本地
docker build -f ./docker_env/django/DockerfileBuild -t xzj746753491/python38-base-algorithm-engine:latest .
# 上传到Docker Hub
docker push xzj746753491/python38-base-algorithm-engine:latest
~~~

### 运行引擎

~~~
docker build -f ./docker_env/django/Dockerfile -t algorithm-engine-django .
~~~

### 运行celery

~~~
docker build -f ./docker_env/celery/Dockerfile -t algorithm-engine-celery .
~~~

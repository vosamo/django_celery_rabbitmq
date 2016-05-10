## 项目说明

简单模拟celery和rabbitmq在django工程中的配置和使用。celery任务队列用来解决大并发情况下web后台的批量操作或者比较耗时的后台操作，以改善前端用户体验。通过队列的方式把这些操作扔给后台的worker处理，不必等待worker处理完任务，快速给前端响应。

该工程的功能：

前端发起请求，执行一个耗时的后台操作。该操作写成任务函数，放入任务队列；后台worker执行任务。

rabbitmq充当中间人broker。

任务结果保存在rabbitmq中。

任务拥有唯一的id，可以通过id来查询任务执行结果。

## 依赖描述

- Django 1.8.2
- django-rest-framework 3.1.2
- Celery 3.1.23
- django-celery 3.1.17
- RabbitMQ-server 3.3.5-17.el7

安装方式：rabbitmq-server用yum安装；其余的用pip安装。

## 使用说明

将仓库克隆到本地，解压缩。打开两个shell终端，进入django_celery_rabbitmq目录。

执行python manage.py migrate，同步数据库。

启动worker：在一个终端中执行`python manage.py celery worker --loglevel=info`

启动server：在另一个终端中执行`python manage.py runserver`

在浏览器中访问`http://127.0.0.1:8000`即可看到 "Task id is:51275290-4e50-43a0-8596-c68ab9301d7c"。

然后访问`http://127.0.0.1:8000/51275290-4e50-43a0-8596-c68ab9301d7c`可以看到任务的执行结果。

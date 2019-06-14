# flask-message


初学flask框架，边学边做写了一个问答网站，使用python3所写

需要的python库

pip install flask

pip install flask_sqlalchemy

pip install flask_migrate

pip install flask_script

需要做一下脚本数据迁移

在项目目录下，进入控制台输入命令


1.初始化迁移文件

python manage.py db init

2.将模型添加到迁移文件

python manage.py db migrate

3.迁移文件中的模型映射到数据库中

python manage.py db upgrade

运行

python manage.py runserver --host 0.0.0.0 --port 80

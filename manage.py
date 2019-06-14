#coding: utf8
#!/usr/bin/env python3

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from icbc import app
from exts import db
from models import User,Question,Answer


manager = Manager(app)
#使用Migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
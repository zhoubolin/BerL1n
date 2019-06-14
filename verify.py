from models import User
from flask import Flask,request,redirect,url_for,session,g,flash
import time
from exts import db
#注册验证

def validate(telephone, password1, username=None, password2=None):
    user = User.query.filter(User.telephone == telephone).first()
    if password2:
        if user:
            return u'该手机号已被注册，请更换手机号码!'
        else:
            if len(telephone) != 11:
                return u'手机号格式不正确！'
            elif username == '':
                return u'用户名不能为空！'
            elif password1 == '':
                return u'密码不能为空！'
            elif password1 != password2:
                return u'两次密码不一致'
            else:
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                time.sleep(1)
                return u'注册成功'


    elif telephone and password1:
        if user and user.check_password(password1):
            session['user_id'] = user.id
            #如果想在31天内都不需要登录
            session.permanent = True
            time.sleep(0.5)
        else:    
            return u'手机号码或密码错误，请确认后再登录！'


    else:
        return u'请完善信息！'

    
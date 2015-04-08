# coding=utf-8

# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'mysite',                           
        'USER': 'root',                        # 你的数据库user
        'PASSWORD': '1992',                    # 你的数据库password
        'HOST': '127.0.0.1',                   # 开发的时候，使用localhost
        'PORT': '3306',                        # 默认3306
    },
}




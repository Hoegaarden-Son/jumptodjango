# Windows 에서 실행
. .\myvenv\Scripts\activate

# debug mode 관련
- exclude 한다는 NAME 만 잘 활용하면, debug가 혹시 TRUE 가 되더라도.. 방지할수있을지도...?
- As a security measure, Django will not include settings that might be sensitive, such as SECRET_KEY.
https://docs.djangoproject.com/en/4.2/ref/settings/#debug


# 장고 앱 만들기
> django-admin startapp pybo

# 장고 data type (field)
https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

# model 변경 후, migrate
- makemigrations 명령은 모델을 생성하거나 모델에 변화가 있을 경우에 실행해야 하는 명령
- 실제 테이블 작업은 migrate 명령을 통해서만 가능
> python manage.py makemigrations

-  migrate 명령을 실행하기 전에 실제 어떤 쿼리문이 실행되는지:
> python manage.py sqlmigrate pybo 0001

# 장고 쉘
> python manage.py shell

# 장고 DB Query
https://docs.djangoproject.com/en/4.0/topics/db/queries/


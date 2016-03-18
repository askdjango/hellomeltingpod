
# Django Azure WebApp Project Template

 * `myazureproject` 로 지정된 부분은 생성할 "Azure 프로젝트 명" 으로 입력해주세요.
 * `myproject` 로 지정된 부분은 생성할 "Django 프로젝트 명" 으로 입력해주세요.


## Azure 프로젝트 생성

[Azure Portal](https://portal.azure.com/#blade/HubsExtension/BrowseAllResourcesBlade) 에서 생성하거나, azure-cli 를 통해 생성할 수 있다.

    쉘> azure site create myazureproject --location "East Asia"


## 로컬에 파이썬 3.4 이상을 설치하고, Django 설치

    pip install django


## 프로젝트 생성

    쉘> django-admin startproject --extension config \
        --template=https://github.com/askdjango/django-azurewebapp-template/archive/master.zip \
        myproject

    쉘> cd myproject
    쉘> python manage.py migrate


## 배포

 * 생성한 프로젝트를 github 에 올리기
 * [Azure Portal](https://portal.azure.com/#blade/HubsExtension/BrowseAllResourcesBlade) 의 생성한 WebApp 프로젝트 페이지
    * Publishing -> Deployment Source 에서 Github 를 선택하고, github 에 등록한 프로젝트를 선택
    * Publishing -> Deployment Source 에서 Sync 를 선택하면, 배포가 수행됨.


## WebApp 에서 관리자계정 생성 management 명령 실행하기

https://myazureproject.scm.azurewebsites.net 를 통해 디버그 콘솔을 띄웁니다.

    CMD> cd site\wwwroot
    CMD> env\Scripts\python manage.py shell --settings=myazureproject.settings.azure_webapp
    파이썬 쉘>  from django.contrib.auth import get_user_model
    파이썬 쉘> User = get_user_model()
    파이썬 쉘> User.objects.create_superuser('adminuesrname', 'adminemail@example.com', 'adminpassword')
    파이썬 쉘> exit()


# 향후 시도해볼 것들

 * `Azure Storage` 에 업로드되는 파일들 저장하기
 * `Azure MySQL Database`
 * `Azure RedisCache` 에 캐싱하기


# 유용한 azure-cli 커맨드

    azure login
    azure site list
    azure site show <webapp_name>
    azure site create meltingdjango --location "East Asia"


# Links

## Azure

 * [Azure WebApp 공식사이트](https://azure.microsoft.com/ko-kr/services/app-service/web/)
 * [Azure Portal](http://portal.azure.com)

## 여러분의 파이썬/장고 페이스메이커가 되어드리겠습니다.

 * [AskDjango 공식 웹사이트](http://ask.festi.kr)
 * [페이스북 그룹](http://facebook.com/groups/askdjango) : Django 에 대한 궁금증을 풀어가세요. ;)
 * [페이스북 페이지](http://facebook.com/askdjango)
 * [ask@festi.kr](mailto:ask@festi.kr)

[![AskDjango](readme/askdjango-allieus.png)](http://facebook.com/askdjango)


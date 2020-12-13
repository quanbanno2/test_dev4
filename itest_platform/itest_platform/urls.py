"""itest_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from project_manage.views import login_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', login_views.hello),

    path('', login_views.index),
    path('index/', login_views.index),
    path('accounts/login/', login_views.index),

    # path('manage/', views.manage),
    path("manage/", include('project_manage.urls')),

    path('logout/', login_views.logout),

    # 用例管理
    path("case/", include('case_manage.urls')),

    # 任务管理
    path("task/", include('task_manage.urls')),
    
    # 接口的管理
    path("api/", include('api_manage.urls')),


]


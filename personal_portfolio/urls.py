"""personal_portfolio URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("passwordgenerator/home1/",views.home1,name="home1"),
    path("passwordgenerator/aboutus1/",views.aboutus1,name="aboutus1"),
    path("passwordgenerator/password/",views.password,name="password"),
    path('blog/', include('blog.urls')),

    #todo
    #path('todo/admin', admin.site.urls),
    #AUTH_PASSWORD_VALIDATORS
    path('todo/signup/', views.signupuser, name='signupuser'),
    path('todo/login/', views.loginuser,name='loginuser'),
    path('todo/logout/', views.logoutuser,name='logoutuser'),

    #Todos
    path('todo/home2',views.home2, name='home2'),
    path('todo/create/',views.createtodos, name='createtodos'),
    path('todo/current/',views.currenttodos, name='currenttodos'),
    path('todo/completed/',views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>',views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete',views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete',views.deletetodo, name='deletetodo'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

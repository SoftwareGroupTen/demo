
from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [
    path('', views.主页, name = '主页'),
    path('login/', views.登录, name = '登录'),
    path('logout/', views.登出, name = '登出'),
    path('register/', views.注册, name = '注册'),
    path('addcourse/', views.addcourse, name = 'addcourse'),
    path('joincourse/', views.joincourse, name = 'joincourse'),
    path('coursedetail/<int:id>',views.coursedetail, name = 'coursedetail'),
    path('coursedelete/<int:id>',views.coursedelete, name = 'coursedelete'),
    path('addassistant/<int:id>',views.addassistant, name = 'addassistant'),
    path('upload/<int:id>/',views.upload,name = 'upload'),
]

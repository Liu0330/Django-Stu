from django.urls import path
from . import views#当前目录
from django.conf.urls import url
urlpatterns = [
 url(r'^$',views.index),
 url(r'(\d+)/(\d+)',views.detail),

 url(r'^grades/$', views.grades),
 url(r'^students/$', views.students),

url(r'^grades/(\d+)$', views.gradesStudents),

]
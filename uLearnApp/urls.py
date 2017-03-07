from django.conf.urls import url, include

from .views import index,lecture,login

urlpatterns = [
    url(r'^$', index.anaSayfa, name='index'),
    url(r'lectures', lecture.lecture, name='index'),
    url(r'login', login.login, name='login'),
]

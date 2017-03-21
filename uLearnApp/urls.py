from django.conf.urls import url, include

from .views import index,lecture,login,register

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'lectures', lecture.lecture, name='index'),
    url(r'login', login.login, name='login'),
    url(r'register', register.register, name='register'),
]

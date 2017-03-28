from django.conf.urls import url, include

from .views import index,lecture,login,register,panel,searchresult,course_content

urlpatterns = [
    url(r'^$', index.anaSayfa, name='index'),
    url(r'lectures', lecture.lecture, name='index'),
    url(r'login', login.login, name='login'),
    url(r'register', register.register, name='register'),
    url(r'panel', panel.panel, name='panel'),
    url(r'searchresult', searchresult.searchresult, name='searchresult'),
    url(r'course_content', course_content.course_content, name='course_content')


]

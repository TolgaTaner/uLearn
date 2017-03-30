from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index,lecture,login,register,searchresult,course_content,courseInstructor,videoupload

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'lectures', lecture.lecture, name='index'),
    url(r'login', login.auth_login, name='login'),
    url(r'register', register.register, name='register'),
    url(r'searchresult', searchresult.searchresult, name='searchresult'),
    url(r'course_content', course_content.course_content, name='course_content'),
    url(r'courseInstructor', courseInstructor.courseInstructor, name='courseInstructor'),
    url(r'videoupload',videoupload.videoupload, name = 'videoupload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

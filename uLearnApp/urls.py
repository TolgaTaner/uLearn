from django.conf.urls import url, include

from .views import index,lecture

urlpatterns = [
    url(r'^$', index.anaSayfa, name='index'),
    url(r'lectures', lecture.lecture, name='index'),

]

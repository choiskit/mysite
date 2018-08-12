from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    url(r'^sendmail/$',views.send_mail,name='sendmail'),
    url(r'^author_add/$',views.author_add,name='author_add'),
    url(r'^publisher_add',views.publisher_add,name='publisher_add'),
    url(r'^publisher/(?P<publisher_id>[0-9]+)/update$',views.publisher_update,name='publisher_update'),
]

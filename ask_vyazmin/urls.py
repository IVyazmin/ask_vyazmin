from django.conf.urls import url
from django.contrib import admin
from ask_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<page_number>[0-9]+)/$', views.index, name = 'index'),
    url(r'^hot/$', views.hot, name = 'hot'),
    url(r'^hot/(?P<page_number>[0-9]+)/$', views.hot, name = 'hot'),
    url(r'^tag/(?P<tag_name>[-\w]+)/$', views.tag, name = 'tag'),
    url(r'^tag/(?P<tag_name>[-\w]+)/(?P<page_number>[0-9]+)/$', views.tag, name = 'tag'),
    url(r'^question/(?P<question_number>[0-9]+)/$', views.question, name = 'question'),
    url(r'^question/(?P<question_number>[0-9]+)/(?P<page_number>[0-9]+)/$', views.question, name = 'question'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^ask/$', views.ask, name = 'ask'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^setting/$', views.setting, name = 'setting'),

    url(r'^like/$', views.like, name = 'like'),
    url(r'^dislike/$', views.dislike, name = 'dislike'),
    url(r'^like_answer/$', views.like_answer, name = 'like_answer'),
    url(r'^dislike_answer/$', views.dislike_answer, name = 'dislike_answer'),
    url(r'^correct/$', views.correct, name = 'correct'),
]

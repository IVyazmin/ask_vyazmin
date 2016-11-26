"""ask_vyazmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ask_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/$', views.application),

    
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
    url(r'^setting/$', views.setting, name = 'setting'),
]

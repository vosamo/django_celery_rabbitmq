from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^$', views.Hello.as_view()),
    url(r'^(?P<uuid>[\w\d-]+)/$', views.TaskState.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]

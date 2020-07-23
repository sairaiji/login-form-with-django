from django.urls import path
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
    path('', views.index),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'), 
]



from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index),
    url(r'^logout/$', LogoutView.as_view(template_name= 'index.html'), name='logout'),
]



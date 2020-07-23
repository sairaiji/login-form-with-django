
from django.conf.urls import url
from django.contrib import admin
from testapp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_account, name='create_account'),
    url(r'^login/$', views.account_login, name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name= 'index.html'), name='logout'),
]
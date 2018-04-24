"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from accounts import views as accounts_views
from hire import views as hire_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hire_views.mainee,name = 'maiee'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^services/$', hire_views.home, name='home'),
    url(r'^services/new/$', hire_views.add_service, name='new_service'),
    url(r'^services/(?P<pk>\d+)/$', hire_views.list_services, name='serve_list'),
    url(r'^services/(?P<pk>\d+)/new/$', hire_views.list_services_new, name='new_serve_list'),
    url(r'^services/(?P<pk>\d+)/delete/$', hire_views.delete_main, name='delete'),
    url(r'^services/(?P<pk>\d+)/(?P<Service_category_pk>\d+)/review/$', hire_views.review, name='review'),
    url(r'^services/(?P<pk>\d+)/(?P<Service_category_pk>\d+)/review/new/$', hire_views.review_new, name='review_new'),
    url(r'^worker_page/(?P<pk>\d+)/$', hire_views.worker_page, name='worker_page'),
       
]

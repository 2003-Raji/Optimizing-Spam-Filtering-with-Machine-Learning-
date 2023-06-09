"""email_spam_detection URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from user import views as user_views
from email_admin import views as admin_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$',user_views.index,name="index"),
    url('user/register', user_views.register, name="register"),
    url('user/userpage',user_views.userpage,name="userpage"),
    url('user/viewmailpage',user_views.viewmailpage,name="viewmailpage"),
    url('user/spampage',user_views.spampage,name="spampage"),
    url('user/logout/$', user_views.logout, name='logout'),
    url('user/delete/(?P<pk>\d+)/$',user_views.deleteobj,name="deleteobj"),
    url('user/spamdelete/(?P<pk>\d+)/$',user_views.spamdeleteobj,name="spamdeleteobj"),
    url('user/mydetails',user_views.mydetails,name="mydetails"),
    url('user/updatemydetails',user_views.updatemydetails,name="updatemydetails"),
    url('user/feedback',user_views.feedback,name="feedback"),

    url('login',admin_views.login,name="login"),
    url('admin_page',admin_views.admin_page,name="admin_page"),
    url('analysis_page',admin_views.analysis_page,name="analysis_page"),
    url('categoryanalysis/(?P<chart_type>\w+)',admin_views.categoryanalysis_chart,name="categoryanalysis_chart"),
    url('admin/delete/(?P<pk>\d+)/$',admin_views.analysisdelete,name="analysisdelete"),
    url('admin/viewfeedback', admin_views.viewfeedback, name="viewfeedback"),

]
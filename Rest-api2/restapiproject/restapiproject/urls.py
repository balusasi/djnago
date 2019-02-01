from django.conf.urls import include, url
from django.contrib import admin
from restapiapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'restapiproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$',views.login),
    url(r'insert/',views.savedetails),
    url(r'^api',views.loginapiview.as_view()),
]

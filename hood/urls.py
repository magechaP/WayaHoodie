from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
url(r'^$',views.choose_hood,name='choose_hood'),
url(r'^setup/hood$',views.setup_hood, name='setup_hood'),
url(r'^hood/profile/(\d+)$',views.setup_profile,name='setup_profile'),
url(r'^setup/hood/profile/',views.setup_profile_hood,name='setup_profile_hood'),
url(r'^home/(\d+)$',views.home,name="home"),
url(r'^profile/(\d+)$',views.user_profile,name='profile'),
url(r'^profile/update/(\d+)$',views.update_profile,name='update_profile'),
url(r'^business/(\d+)$',views.business, name='business'),
url(r'^leave/hood$', views.leave_hood, name='left')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
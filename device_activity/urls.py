from django.conf.urls import url
from device_activity import views

app_name = 'device_activity'
urlpatterns = [
    url(r'^activity/$', views.DeviceActivityListView.as_view(), name='activity'),
    url(r'^activity/(?P<pk>[-\w]+)', views.DeviceActivityDetailView.as_view(), name = 'device'),
]

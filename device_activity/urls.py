from django.conf.urls import url
from modules.account_management.device_activity import views

app_name = 'device_activity'
urlpatterns = [
    url(r'^activity/$', views.DeviceActivityListView.as_view(), name='activity'),
]

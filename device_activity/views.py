from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from modules.account_management.device_activity.models import DeviceActivity

class DeviceActivityListView(LoginRequiredMixin, ListView):
    model = DeviceActivity
    template_name = 'account_management/device_activity/device_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
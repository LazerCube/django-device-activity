from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from device_activity.models import DeviceActivity

class DeviceActivityListView(LoginRequiredMixin, ListView):
    model = DeviceActivity
    template_name = 'device_activity/device_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-created_at')

class DeviceActivityDetailView(DetailView):
    model = DeviceActivity
    template_name = 'device_activity/device_detail.html'

    def get_queryset(self):
        queryset = super(DeviceActivityDetailView, self).get_queryset()
        return queryset.filter(user=self.request.user)

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)

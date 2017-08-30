import datetime

from modules.account_management.device_activity.models import DeviceActivity

class DeviceMiddleware(object):
    """
        Save the Ip address if does not exist
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')

            try:
                DeviceActivity.objects.get(ip_address=ip)
            except DeviceActivity.DoesNotExist:
                ua_string = request.META.get('HTTP_USER_AGENT', '')
                device = DeviceActivity(ip_address=ip, user=request.user, ua_string=ua_string)
                device.save()
        return None

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from user_agents import parse

class DeviceActivity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    ip_address = models.GenericIPAddressField()
    ua_string = models.CharField(max_length=256, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_user_agent(self):
        return parse(self.ua_string)

    def get_browser(self):
        user_agent = self.get_user_agent()
        return user_agent.browser

    def get_os(self):
        user_agent = self.get_user_agent()
        return user_agent.os

    def get_device(self):
        user_agent = self.get_user_agent()
        return user_agent.device

    @property
    def is_mobile(self):
        return self.get_user_agent().is_mobile

    @property
    def is_tablet(self):
        return self.get_user_agent().is_tablet

    @property
    def is_touch_capable(self):
        return self.get_user_agent().is_touch_capable

    @property
    def is_pc(self):
        return self.get_user_agent().is_pc

    @property
    def is_bot(self):
        return self.get_user_agent().is_bot

    def __unicode__(self):
        return str(self.get_user_agent())

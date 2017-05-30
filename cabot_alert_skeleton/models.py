from cabot.cabotapp.alert import AlertPlugin
from cabot.cabotapp.alert import AlertPluginUserData
from django.db import models
# from cabot.plugins.models import AlertPlugin
# from django import forms
# from os import environ as env

from logging import getLogger
logger = getLogger(__name__)

class SkeletonAlertUserData(AlertPluginUserData):
    name = "Skeleton Plugin"
    favorite_bone = models.CharField(max_length=50, blank=True)

class SkeletonAlert(AlertPlugin):
    name = "Skeleton"
    author = "Jack Skellington"

    def send_alert(self, service, users, duty_officers):
        """Implement your send_alert functionality here."""
        return

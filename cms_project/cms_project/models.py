from django.db import models
from cms.models import CMSPlugin


class HeaderPluginModel(CMSPlugin):
    heading = models.CharField(max_length=20, default='True')

    def __str__(self):
        return self.heading
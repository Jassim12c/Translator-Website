from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Translate(models.Model):
    sentence = models.TextField(blank=False, verbose_name="sentence")

    def get_absolute_url(self):
        return reverse('main:translate')

    def __str__(self):
        return "The sentence is: " + str(self.sentence)

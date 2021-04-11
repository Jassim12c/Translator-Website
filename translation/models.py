from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Translate(models.Model):
    sentence = models.TextField(blank=False, help_text=_("Please enter a sentence"), verbose_name=_("sentence"))

    def get_absolute_url(self):
        return reverse('main:translate')

    def __str__(self):
        return "The sentence is: " + str(self.sentence)

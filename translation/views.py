
from django.http import HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse


from . import models
from . import forms


def translate(request):

    sentence = models.Translate.objects.all()
    form = forms.TranslateForm()

    if request.method == "POST":
        form = forms.TranslateForm(request.POST)
        if form.is_valid():
            sen = form.save(commit=False)
            sen.save()
            return HttpResponseRedirect(reverse('main:translate'))
    return render(request, 'forms/translate_form.html', {'sentence': sentence, 'form': form})

def clear_sen(request):
    words = models.Translate.objects.all()
    words.delete()
    return redirect("main:translate")

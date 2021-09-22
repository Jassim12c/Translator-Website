from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader


from . import models
from . import forms

def translate(request):

    form = forms.TranslateForm()
    template = loader.get_template('forms/translate_form.html')

    if request.method == "POST":
        sentence = request.POST['sentence']
        return render(request, 'forms/translate_form.html', {'sentence': sentence, 'form': form})
    return HttpResponse(template.render({'form': form}, request))

def clear_sen(request):
    words = models.Translate.objects.all()
    words.delete()
    return redirect("main:translate")

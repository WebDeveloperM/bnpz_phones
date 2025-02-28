from django.shortcuts import render
from . import forms
from .models import Phone
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from . import forms
from datetime import datetime


def home_view(request):
    return render(request, 'main/index.html')


from django.db.models import F

from django.db import connection

# def phones(request):
#     phones = Phone.objects.select_related('section__departament').order_by('section__departament__number')
#     print(phones)
#     return render(request, 'main/phones.html', {'phones': phones})


from django.core.paginator import Paginator


def phones(request):
    phones = Phone.objects.select_related('section__departament').order_by('section__departament__number')

    from django.core.cache import cache
    cache.clear()

    return render(request, 'main/phones.html', {'phones': phones})


def sign_in(request):
    if request.method == 'POST':
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignInForm()
    current_year = datetime.now().year
    return render(request, 'main/sign_in.html', {'form': form, "current_year": current_year})


def sign_out(request):
    logout(request)
    return redirect('sign_in')

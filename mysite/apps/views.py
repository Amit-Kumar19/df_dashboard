import pandas as pd
from django.shortcuts import render
from .models import *
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# to validate a user with authentication system
from django.contrib.auth import authenticate, login, logout
# to restrict user to view a particular page
from django.contrib.auth.decorators import login_required
from .decorator import authenticated_user
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='login')
def hello(request):
    meta_val = MetaDetails.objects.all().order_by('-date_created')
    page = request.GET.get('page', 1)
    paginator = Paginator(meta_val, 10)
    try:
        meta_val = paginator.page(page)
    except PageNotAnInteger:
        meta_val = paginator.page(1)
    except EmptyPage:
        meta_val = paginator.page(paginator.num_pages)
    context = {'keywords': meta_val}

    return render(request, 'apps/dashboard.html', context)


@authenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'apps/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def geeks_view(request, pk):
    info = DbConnectionInfo.objects.filter(tbl_name=pk)
    db_name = [item.db_name for item in info][0]
    df = pd.read_excel(f"data/{db_name}.{pk}.xlsx", sheet_name=0, nrows=5)
    col_names = df.columns.tolist()
    data = df.values.tolist()
    context = {'data': data, 'col_names': col_names}
    return render(request, "apps/preview.html", context)

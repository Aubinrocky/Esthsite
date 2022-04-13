from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
from .models import *
from .forms import CAForm, ProfileForm
import pandas as pd


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Nom ou mot de passe incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    current_user = request.user
    CAs_current_user = CA.objects.filter(author=current_user).values()

    CAs = CA.objects.all()
    result = CA.objects.filter(author=current_user).annotate(Sum('montant'))

    context = {'result': result}
    print([i.montant for i in result])
    # context = {'CAs': CAs, 'CAs_current_user': CAs_current_user,
    #            'df1': df1, 'df2': df2}
    # context['qs'] = CA.objects.all()
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def comparatif(request):
    CAs = CA.objects.all()

    return render(request, 'accounts/comparatif.html', {'CAs': CAs})


@login_required(login_url='login')
def mescomptes(request):
    current_user = request.user
    CAs_current_user = CA.objects.filter(author=current_user)
    return render(request, 'accounts/mescomptes.html', {'CAs_current_user': CAs_current_user})


@login_required(login_url='login')
def addCA(request):
    form = CAForm()
    if request.method == 'POST':
        form = CAForm(request.POST)
        if form.is_valid():
            new_CA = form.save(commit=False)
            new_CA.author = request.user  # User posting the form
            new_CA.save()
            return redirect('/mescomptes')

    context = {'form': form}
    return render(request, 'accounts/add_ca.html', context)


@login_required(login_url='login')
def editCA(request, pk):
    ca = CA.objects.get(id=pk)
    form = CAForm(instance=ca)
    if request.method == 'POST':
        form = CAForm(request.POST, instance=ca)
        if form.is_valid():
            form.save()
            return redirect('/mescomptes')
    context = {'form': form}
    return render(request, 'accounts/add_ca.html', context)


@login_required(login_url='login')
def deleteCA(request, pk):
    ca = CA.objects.get(id=pk)
    print(ca)
    if request.method == 'POST':
        ca.delete()
        return redirect('/mescomptes')
    context = {'item': ca}
    return render(request, 'accounts/delete_ca.html', context)


@login_required(login_url='login')
def userProfile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def editProfile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    context = {'form': form, 'current_user': current_user}
    return render(request, 'accounts/profile.html', context)

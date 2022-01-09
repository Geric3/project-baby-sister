from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse, request, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .forms import UserRegistration, UserEditForm, ContactForm, SouscribeForm3
from .models import NewRecrueRegistration

from . import forms

# Create your views here.

@login_required
def homePage(request):
    return render(request, 'recrues/homepage.html', locals())

#def login(request):

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'recrues/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'recrues/register.html', context=context)

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            comen = form.save(commit=False)
            comen.usern = request.user
            comen.message_date = timezone.now
            comen.save()
            return redirect('/homepage/')
    else:
        form = ContactForm()
    return render(request, 'recrues/contactpage.html', {'form': form})

@login_required
@csrf_exempt
def subcribe_view(request):
    form = forms.SouscribeForm3()
    if request.method == 'POST':
        form = forms.SouscribeForm3(request.POST , request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.uploader = request.user
            img.user = User.objects.get(id=request.user.id)
            img.register_date = timezone.now
            img.save()
            return redirect('/homepage/')
    else:
        form = SouscribeForm3()
    return render(request, 'recrues/inscription.html', {'form': form})

@login_required
def list_view(request):
    recru = NewRecrueRegistration.objects.all()
    return render(request, 'recrues/listrecrue.html', {'recru': recru})

@login_required
@csrf_exempt
def update_subcribe_view(request):
    form = forms.SouscribeForm3()
    if request.method == 'POST':
        form = forms.SouscribeForm3(request.POST , request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.uploader = request.user
            if NewRecrueRegistration.objects.filter(user_id=request.user.id).exists():
                for e in NewRecrueRegistration.objects.filter(user_id=request.user.id):
                    e.picture = img.picture
                    e.cv = img.cv 
                    e.telephone = img.telephone
                    e.mode = img.mode
                    e.message = img.message
                    e.save()
                    return redirect('/homepage/')
            else:
                print( 'Vous n avez pas de compte. Utulisez le formulaire ci-dessous pour vous enregistrer.')
                return redirect('/homepage/enrollment/')
            
             
            
    else:
        form = SouscribeForm3()
    return render(request, 'recrues/update_inscription.html', {'form': form})
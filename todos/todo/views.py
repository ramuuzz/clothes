from django.shortcuts import render, redirect
from .forms import ShirtForm, PantsForm, JacketForm
from django.contrib.auth import authenticate, login as login1, logout as logout1
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return render(request,'login.html')
    return render(request, 'register.html')
def home(request):
    
    return render(request, 'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login1(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'login.html')
def logout(request):
    logout1(request)#logout user defined func and logout django func should have different name
    return redirect('home')

@login_required
def shirt(request):  
    if request.method == 'POST':
        form = ShirtForm(request.POST, request.FILES)
        if form.is_valid():
            shirt = form.save(commit=False)
            shirt.user = request.user
            shirt.save()
            return redirect('shirt')
    else:
        form = ShirtForm()
    shirts = request.user.shirts.all()
    return render(request, 'shirt.html', {'form': form, 'shirts': shirts})
# Create your views here.

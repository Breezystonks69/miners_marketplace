from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Miner
from .forms import MinerForm

def index(request):
    miners = Miner.objects.all()
    return render(request, 'marketplace/index.html', {'miners': miners})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'marketplace/register.html', {'form': form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    miners = Miner.objects.filter(seller=request.user)
    return render(request, 'marketplace/dashboard.html', {'miners': miners})

def list_miner(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = MinerForm(request.POST, request.FILES)
        if form.is_valid():
            miner = form.save(commit=False)
            miner.seller = request.user
            miner.save()
            return redirect('dashboard')
    else:
        form = MinerForm()
    return render(request, 'marketplace/list_miner.html', {'form': form})

def miner_detail(request, miner_id):
    miner = Miner.objects.get(id=miner_id)
    return render(request, 'marketplace/miner_detail.html', {'miner': miner})
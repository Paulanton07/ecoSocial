from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Post, Connection
from .forms import ProfileForm, CustomUserCreationForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, content=content)
            messages.success(request, 'Post created successfully')
            return redirect('home')
    return render(request, 'create_post.html')

@login_required
def connect(request, username):
    user_to_connect = get_object_or_404(User, username=username)
    if request.user != user_to_connect:
        Connection.objects.get_or_create(user_from=request.user, user_to=user_to_connect)
        messages.success(request, f'Connected with {username}')
    return redirect('profile')

@login_required
def connections(request):
    connections_from = Connection.objects.filter(user_from=request.user)
    connections_to = Connection.objects.filter(user_to=request.user)
    return render(request, 'connections.html', {
        'connections_from': connections_from,
        'connections_to': connections_to
    })

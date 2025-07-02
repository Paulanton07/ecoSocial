from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Post, Connection, Stock
from .forms import ProfileForm, CustomUserCreationForm

def home(request):
    latest_stock = Stock.objects.order_by('-date_added')[:5]
    # Dashboard/homepage view
    return render(request, 'homepage.html', {'latest_stock': latest_stock})

def posts(request):
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

def workspace(request):
    results = None
    notepad = request.session.get('notepad', '')
    saved_notes = request.session.get('saved_notes', [])
    user_notes = None
    if request.user.is_authenticated:
        if not hasattr(request.user, 'profile'):
            Profile.objects.get_or_create(user=request.user)
        if not hasattr(request.user.profile, 'workspace_notes'):
            request.user.profile.workspace_notes = ''
        user_notes = request.user.profile.workspace_notes.split('||') if request.user.profile.workspace_notes else []
    if request.method == 'POST':
        if 'save_note' in request.POST:
            notepad = request.POST.get('notepad', '')
            if request.user.is_authenticated:
                # Save persistent notes for logged-in users
                notes = request.user.profile.workspace_notes or ''
                notes_list = notes.split('||') if notes else []
                if notepad.strip():
                    notes_list.append(notepad.strip())
                    request.user.profile.workspace_notes = '||'.join(notes_list)
                    request.user.profile.save()
                user_notes = notes_list
            else:
                # Save note to a list in session for guests
                saved_notes = request.session.get('saved_notes', [])
                if notepad.strip():
                    saved_notes.append(notepad.strip())
                    request.session['saved_notes'] = saved_notes
            request.session['notepad'] = ''
            notepad = ''
        elif 'delete_note' in request.POST:
            note_index = int(request.POST.get('delete_note'))
            if request.user.is_authenticated:
                notes_list = user_notes
                if 0 <= note_index < len(notes_list):
                    notes_list.pop(note_index)
                    request.user.profile.workspace_notes = '||'.join(notes_list)
                    request.user.profile.save()
                user_notes = notes_list
            else:
                if 0 <= note_index < len(saved_notes):
                    saved_notes.pop(note_index)
                    request.session['saved_notes'] = saved_notes
        else:
            project_type = request.POST.get('project_type')
            try:
                length = float(request.POST.get('length', 0))
                width = float(request.POST.get('width', 0))
                height = float(request.POST.get('height', 0) or 0)
            except (TypeError, ValueError):
                length = width = height = 0
            wood_type = request.POST.get('wood_type')
            if project_type in ['deck', 'custom'] and length and width:
                area = length * width
                stock = Stock.objects.filter(wood_type=wood_type).order_by('price').first()
                plank_area = 1.2 * 0.1
                quantity = int((area / plank_area) + 0.999)
                cost = quantity * (stock.price if stock and stock.price else 0)
            elif project_type == 'box' and length and width and height:
                volume = length * width * height
                stock = Stock.objects.filter(wood_type=wood_type).order_by('price').first()
                plank_volume = 1.2 * 0.1 * 0.02
                quantity = int((volume / plank_volume) + 0.999)
                cost = quantity * (stock.price if stock and stock.price else 0)
            else:
                quantity = 0
                cost = 0
            results = {
                'project_type': project_type.title() if project_type else '',
                'length': length,
                'width': width,
                'height': height if height else None,
                'wood_type': wood_type.title() if wood_type else '',
                'quantity': quantity,
                'cost': f"{cost:.2f}"
            }
    return render(request, 'workspace.html', {
        'results': results,
        'notepad': notepad,
        'saved_notes': user_notes if request.user.is_authenticated else saved_notes,
        'user_is_authenticated': request.user.is_authenticated
    })

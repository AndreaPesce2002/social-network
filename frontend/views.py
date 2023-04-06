from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm, PostForm
from django.contrib import messages
from .models import Utente, Post


def ele(request):
    follower_ids = Utente.objects.filter(id=request.COOKIES.get('id_utente')).values_list('followers__id', flat=True)
    utente=Utente.objects.get(id=request.COOKIES.get('id_utente'))
    return follower_ids,utente

def index(request):
    if 'id_utente' in request.COOKIES:
        if Utente.objects.filter(id=request.COOKIES.get('id_utente')).exists():
            follower_ids, utente = ele(request)
            return render(request, 'frontend/post.html', {'posts': Post.objects.all().order_by('-like'), 'utente': utente,'seguiti':follower_ids, 'title':'TUTTI I POST'})
        else:
            return login(request)
    else:
        return render(request, 'frontend/post.html', {'posts': Post.objects.all().order_by('-like'), 'title':'TUTTI I POST'})

def profilo(request):
    if 'id_utente' in request.COOKIES:
        if Utente.objects.filter(id=request.COOKIES.get('id_utente')).exists():
            follower_ids, utente = ele(request)
            return render(request, 'frontend/post.html', {'posts': Post.objects.filter(creatore=request.COOKIES.get('id_utente')), 'utente': utente, 'seguiti':follower_ids, 'pagina': 'frontend/profilo.html'})
        else:
            return login(request)
    else:
        return login(request)
 
    
def seguiti(request):
    if Utente.objects.filter(id=request.COOKIES.get('id_utente')).exists():
        follower_ids, utente = ele(request)
        posts = Post.objects.filter(creatore_id__in=follower_ids)
        return render(request, 'frontend/post.html', {'posts': posts, 'utente': utente,'seguiti':follower_ids, 'title':'SEGUITI'})
    else:
        return login(request)

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if(user):
                # fai qualcosa dopo la registrazione, ad esempio effettua il login
                home=cookies('home',user.id)
                return home
            else:
                messages.error(request, 'il nome utente essite già')
    else:
        user_form = RegisterForm()
    return render(request, 'frontend/register.html', {'user_form': user_form})

def login(request):
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            user = user_form.verifica()
            if user:
                # fai qualcosa dopo la registrazione, ad esempio effettua il login
                home=cookies('home',user.id)
                return home
            else:
                # se l'utente non è stato trovato, mostra un messaggio di errore
                messages.error(request, 'Credenziali non valide')
    else:
        user_form = LoginForm()
    return render(request, 'frontend/login.html', {'user_form': user_form})

def create_post(request):
    if 'id_utente' in request.COOKIES:
        if Utente.objects.filter(id=request.COOKIES.get('id_utente')).exists():
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(user_id=request.COOKIES.get('id_utente'))
                    messages.success(request, 'Post creato con successo!')
                    return redirect('home')
                else:
                    messages.error(request, 'qualcosa è andato storto')
            else:
                form = PostForm()
            return render(request, 'frontend/creaPost.html', {'form': form})
        else:
            return login(request)
    else:
        return login(request)
    
def increment_like(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like += 1
    post.save()
    next_url = request.GET.get('next', None)
    if next_url:
        return redirect(next_url)
    else:
        index()

def iscriviti(request, utente_id, creatore_id):
    utente = Utente.objects.get(id=utente_id)
    utente.followers.add(creatore_id)
    utente.save()
    next_url = request.GET.get('next', None)
    if next_url:
        return redirect(next_url)
    else:
        index()

def iscritto(request, utente_id, creatore_id):
    utente = Utente.objects.get(id=utente_id)
    utente.followers.remove(creatore_id)
    utente.save()
    next_url = request.GET.get('next', None)
    if next_url:
        return redirect(next_url)
    else:
        index()

def cookies(pagina, name):
    response = redirect(pagina)
    
    # Crea i nuovi cookie
    response.set_cookie('id_utente', name)

    return response
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('seguiti', views.seguiti, name="seguiti"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('profilo', views.profilo, name="profilo"),
    path('newPost', views.create_post, name="newPost"),
    path('post/<int:post_id>/like/', views.gestion_like, name='gestion_like'),
    path('utente/<int:utente_id>/<int:creatore_id>/iscriviti/', views.iscriviti, name='iscriviti'),
    path('utente/<int:utente_id>/<int:creatore_id>/iscritto/', views.iscritto, name='iscritto'),
]
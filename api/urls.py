from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('utente', views.UtenteList.as_view(), name='APIutente'),
    path('utente/<int:pk>/', views.UtenteDetail.as_view()),
    path('post', views.PostList.as_view(), name='APIpost'),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
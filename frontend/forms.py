from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .models import Utente, Post

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Utente
        fields = ['nome', 'descrizione', 'password']

    def save(self, commit=True):
        Utente = super().save(commit=False)
        Utente.set_password(self.cleaned_data["password"])
        if commit:
            # verifica se esiste già un utente con lo stesso nome
            if not self.Meta.model.objects.filter(nome=Utente.nome).exists():
                Utente.save()
                return Utente
        return None

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Utente
        fields = ['nome', 'password']

    def verifica(self):
        nome = self.cleaned_data.get('nome')
        password = self.cleaned_data.get('password')
        utente = Utente.objects.filter(nome=nome).first()
        if utente and check_password(password, utente.password):
            return utente
        return None
    
class PostForm(forms.ModelForm):
    post = forms.ImageField(label='Immagine del post')
    descrizione = forms.CharField(label='Descrizione', widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Post
        fields = ['post', 'descrizione']

    def save(self, user_id, commit=True):
        post = super().save(commit=False)
        post.creatore = Utente.objects.filter(id=user_id).first()
        if commit:
            post.save()
            return post
        return None
    
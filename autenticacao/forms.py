from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput)
    birth_date = forms.DateField(label='Data de Nascimento', widget=forms.DateInput)
    username = forms.CharField(label='Usuário')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)
    gender = forms.ChoiceField(label='Gênero', choices=(('M', 'Masculino'), ('F', 'Feminino')))
    photo = forms.ImageField(label='Foto de Perfil')
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email', 'photo', 'birth_date', 'gender']


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput)
    birth_date = forms.DateField(label='Data de Nascimento', widget=forms.DateInput)
    username = forms.CharField(label='Usuário')
    photo = forms.ImageField(label='Foto de Perfil')
    bio = forms.CharField(label='Biografia')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    gender = forms.ChoiceField(label='Gênero', choices=(('M', 'Masculino'), ('F', 'Feminino')))

    class Meta:
        model = UserProfile
        exclude = ['is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions', 'password', 'superuser_status', 'is_superuser']

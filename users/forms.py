from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import CustomUser

#Формы регистрации
class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(widget= forms.PasswordInput(attrs={
        'class': 'form-control shadow-sm p-3 rounded',
        'placeholder': 'Минимум 8 символов'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control shadow-sm p-3 rounded',
        'placeholder': 'Повторите пароль'
    }))
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'image', 'phone_number', 'country')

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control shadow-sm p-3 rounded',
                'placeholder': 'name@example.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control shadow-sm p-3 rounded',
                'maxlength': '11',
                'placeholder': '+79990000000'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control shadow-sm p-3 rounded',
                'placeholder': 'Россия'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control shadow-sm p-3 rounded bg-light',
            }),
        }


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control shadow-sm p-3 rounded',
            'placeholder': 'name@example.com'
        }),
        label='Email адрес'  # Опционально: меняет текст лейбла в шаблоне, если используешь {{ form.username.label }}
    )

    # Переопределяем поле password со стилями
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control shadow-sm p-3 rounded',
            'placeholder': 'Введите пароль'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password1')
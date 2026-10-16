from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


# Create your views here.

class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(user_email) -> None:
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(subject, message, recipient_list)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomUserAuthenticationForm
    success_url = reverse_lazy('catalog:home')

    def form_invalid(self, form):
        print("Ошибки формы:", form.errors)
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    template_name = 'login.html'
    next_page = reverse_lazy('catalog:home')
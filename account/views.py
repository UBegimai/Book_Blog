from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import RegistrationForm, ChangePasswordForm, ForgotPasswordForm

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successful-registration')


class SuccessfulRegistrationView(TemplateView):
    template_name = 'account/success_registration.html'


class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html', {})


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index-page')




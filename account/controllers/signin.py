from urllib import request
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

User = get_user_model()

class signinForm(forms.Form):

    email = forms.CharField(
        widget=forms.EmailInput(), 
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if not user:
            msg = _("Your email and/or Password are invalid.")
            raise ValidationError(msg, code='invalid')

def SigninView(request):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    context= {}
    context['sess_email'] = request.session['sess_email']
    context['form'] = signinForm()

    if request.POST:
        form = signinForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                name = request.user.full_name
                messages.add_message(request,messages.SUCCESS, f'Welcome back {name}')
                del request.session['sess_email']
                destination = request.session['next']
                try:
                    nextURL = request.session['nextURL']
                except:
                    request.session['nextURL'] = None

                nextURL = request.session['nextURL']
                if nextURL:
                    return redirect(nextURL)
                else:
                    if destination:
                        return redirect(f'{destination}')
                return redirect("core:index")
        else:
            context['form'] = form

    return render(request, 'account/signin.html', context)        
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.core.validators import RegexValidator
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from .activate import activationEmail

User = get_user_model()

class subscribeForm(forms.ModelForm):

    email = forms.CharField(
        widget=forms.EmailInput(), 
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )
    alias = forms.CharField(
        label=_("Username"),
        validators=[RegexValidator(r'^[A-Za-z0-9-_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")],
    )
    full_name = forms.CharField(
        label=_("Full Name"),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character (!@#$%)."))]
    )

    class Meta:
        model = User
        fields = ('email', 'alias', 'full_name', 'password')

    def clean_alias(self):
        cleaned_data = super(subscribeForm, self).clean()
        alias = cleaned_data.get("alias")
        if User.objects.filter(alias__iexact=alias).exists():
            msg = f"{alias} is not available!"
            self.add_error('alias', msg)
        return alias

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

def SubscribeView (request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    context= {}
    context['sess_email'] = request.session['sess_email']
    context['form'] = subscribeForm()

    if request.method == "POST":
        form = subscribeForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email'].lower()
            full_name = form.cleaned_data['full_name']
            alias = form.cleaned_data['alias']
            password = form.cleaned_data['password']
            user = authenticate(email=email, full_name=full_name, alias=alias, password=password)
            login(request, user)
            activationEmail(request, user) # Send activation email
            name = request.user.full_name
            messages.add_message(request,messages.SUCCESS, f"Hi {name}, your new account has been created. Click the activation link sent to your email so that we can confirm it is you.")
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
            context['alias'] = request.POST['alias']
            context['full_name'] = request.POST['full_name']

    return render(request, "account/subscribe.html", context)
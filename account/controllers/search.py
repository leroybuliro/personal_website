from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.shortcuts import redirect, render

User = get_user_model()

#####

class authForm(forms.Form):
    email = forms.CharField(
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )

def AuthView(request):
    user = request.user
    if user.is_authenticated:
        destination = request.session['next']
        if destination:
            return redirect(f'{destination}')
        return redirect("core:index")

    context = {}
    form = authForm()
    context['form'] = form
    try:
        context['sess_email'] = request.session['email']
    except:
        request.session['email'] = None
        

    if request.method == 'POST':
        form = authForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            request.session['sess_email'] = email.lower()
            if request.GET.get('next'):
                nextURL = request.GET.get('next')
                request.session['nextURL'] = nextURL

            if User.objects.filter(email__iexact=email).exists():
                return redirect("account:signin")
            else:
                return redirect("account:subscribe")

        else:
            context['form'] = authForm(request.POST, initial=form)

    return render(request, "account/auth.html", context)

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.validators import RegexValidator
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from ..utils import activation_token
from threading import Thread

User = get_user_model()

class pwdResetForm(forms.Form):
    email = forms.CharField(
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(
            r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$',
            message=_("Please enter a valid email"))],
    )

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if not User.objects.filter(email__iexact=email).exists():
            msg = _("Account does not exist")
            raise forms.ValidationError(msg, code="invalid")
        return email

def resetPwdView(request):
    user = request.user
    if user.is_authenticated:
        destination = request.session['next']
        if destination:
            return redirect(f'{destination}')
        return redirect("core:index")

    context = {}
    form = pwdResetForm()
    context['form'] = form

    if request.POST:
        form = pwdResetForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            user = User.objects.get(email__iexact=email)
            resetPwdEmailing(request, user)
            request.session['msg'] = "Thank you for your request. If the username or email \
                you entered matched our records, we have emailed a link you can use to reset \
                    your password. If you do not receive an email then no matching account \
                        was found for the email you provided. Please create a new account."
            return redirect('account:authmsg')

    return render(request, "account/pwdreset.html", context)

class EmailThread(Thread):
    def __init__(self, email):
        self.email = email
        Thread.__init__(self)

    def run(self):
        self.email.send()

def resetPwdEmailing(request, user):
    emailTemplate = render_to_string("emails/emailPwdReset.html", {
        'name': user.full_name,
        'uid': urlsafe_base64_encode(force_bytes(user.uid)),
        'token': activation_token.make_token(user),
        'siteURI': get_current_site(request),
    })
    email = EmailMessage(
        'Ask and you shall receive... a password reset - The Buliro.net Team',
        emailTemplate,
        settings.EMAIL_HOST_USER,
        [request.POST['email'],],
    )
    email.fail_silently=False
    EmailThread(email).start()

def resetPwdDoneEmailing(request, user):
    emailTemplate = render_to_string("emails/emailPwdResetDone.html", {
        'name': user.full_name,
    })
    email = EmailMessage(
        'Your Buliro.net password has been updated',
        emailTemplate,
        settings.EMAIL_HOST_USER,
        [request.POST['email'],],
    )
    email.fail_silently=False
    EmailThread(email).start()

def userVerifyView(request, uidcoded, token):
    uid = force_str(urlsafe_base64_decode(uidcoded))
    user = User.objects.get(uid=uid)

    if user and activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        resetPwdDoneEmailing(request, user)
        request.session['msg'] = "Password successfully changed. You can now login with your new password."
        return redirect('account:authmsg')

    request.session['msg'] = "Password reset failed. Try again later."
    return redirect('account:authmsg')


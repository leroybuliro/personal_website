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

class EmailThread(Thread):
    def __init__(self, email):
        self.email = email
        Thread.__init__(self)

    def run(self):
        self.email.send()

def activationEmail(request, user):
    emailTemplate = render_to_string("emails/emailActivation.html", {
        'name': user.full_name,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': activation_token.make_token(user),
        'siteURI': get_current_site(request),
    })
    email = EmailMessage(
        'Verify Email',
        emailTemplate,
        settings.EMAIL_HOST_USER,
        [request.POST['email'],],
    )
    email.fail_silently=False
    EmailThread(email).start()

class changePwdForm(forms.Form):
    password = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput,
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character (!@#$%)."))]
    )
    password2 = forms.CharField( widget = forms.PasswordInput(), label = _("Re-enter Password"))

    def clean_password(self):
        password = self.cleaned_data('password')
        password2 = self.cleaned_data('password2')
        if password != password2:
            msg = _("Passwords do not match!")
            raise forms.ValidationError(msg, code='Invalid')
        return password

def resetPwdEditView(request, uidcoded, token):
    if request.user.is_authenticated:
        return redirect("core:index")

    context={}
    context['form'] = changePwdForm()

    uid = force_str(urlsafe_base64_decode(uidcoded))
    user = User.objects.get(uid=uid)

    if not user and activation_token.check_token(user, token):
        request.session['msg'] = "Link has expired. Request a new one."
        return redirect('account:authmsg')
        
    if request.POST:
        form = changePwdForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data["password"]
            user.set_password(raw_password)
            user.set_verified = True
            user.save()
            request.session['msg'] = "Password successfully changed."
            return redirect('account:authmsg')

    return render(request, 'account/authReset.html', context)
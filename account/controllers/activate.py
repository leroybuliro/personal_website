from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ..utils import activation_token
from django.contrib.sites.shortcuts import get_current_site
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

def userActivationView(request, uidcoded, token):
    uid = force_str(urlsafe_base64_decode(uidcoded))
    user = User.objects.get(uid=uid)

    if user and activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        request.session['msg'] = "Password successfully changed. You can now login with your new password."
        return redirect('account:authmsg')

    request.session['msg'] = "Email activation failed. Try again later."
    return redirect('account:authmsg')


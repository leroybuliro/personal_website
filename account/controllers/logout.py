from django.contrib.auth import logout
from django.shortcuts import redirect

# from django.contrib import messages

def LogoutView(request, *args, **kwargs):
    logout(request)
    # messages.success(request, 'Successfully logged out!', fail_silently=True)
    destination = request.session['next']
    if destination:
        return redirect(f'{destination}')
    return redirect("core:index")
from django.shortcuts import render

# Error views.

def page404 (request, exception):
    return render(request, 'core/404.html')

def page500 (request):
    return render(request, 'core/serverError.html')

def csrf_failure(request, reason=""):
    # context = {'message': 'some custom messages'}
    return render(request, 'core/csrfError.html')
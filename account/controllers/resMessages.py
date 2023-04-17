from django.shortcuts import render

def AuthMsgView(request):
    msg = request.session['msg']
    return render(request, 'account/authResponse.html', {'msg': msg})
def get_client_ip(request):
    ipaddress = request.META.get('HTTP_X_FORWARDED_FOR')
    if ipaddress:
        ip = ipaddress.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
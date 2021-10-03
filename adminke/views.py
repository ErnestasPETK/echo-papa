from django.shortcuts import redirect


def redirect_auth(request):
    
    response = redirect('/authentication/')
    
    return response
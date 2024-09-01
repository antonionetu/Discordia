from django.shortcuts import render


def set_name(request):
    return render(request, 'set-name.html')

from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'frontend/base.html', context)

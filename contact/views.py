from django.shortcuts import render


def index(request):
    return render(
        request,
        'contact/index.html',
    )


def create(request):
    return render(
        request,
        'contact/create.html',
    )

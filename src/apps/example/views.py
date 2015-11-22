from django.shortcuts import render


def home(request):
    context = {
        'hello': 'Hello word'
    }
    return render(request, 'example/index.html', context)
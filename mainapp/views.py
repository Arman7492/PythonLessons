from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def index(request):
    title = 'Главная страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)


def product(request):
    return render(request, 'product.html')


def products(request):
    return render(request, 'products.html')
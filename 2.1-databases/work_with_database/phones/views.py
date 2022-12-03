from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    response = Phone.objects.all()
    if sort == 'name':
        response = response.order_by("name")
    elif sort == 'min_price':
        response = response.order_by("price")
    elif sort == 'max_price':
        response = response.order_by("-price")
    template = 'catalog.html'
    context = {
        "phones": response
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)

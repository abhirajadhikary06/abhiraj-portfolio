from django.shortcuts import render
from .models import AffiliateProduct, Goodie

def store(request):
    affiliate_product = AffiliateProduct.objects.all()
    goodies = Goodie.objects.all()
    context = {
        'affiliate_products': affiliate_product,
        'goodies': goodies
    }
    return render(request, 'store-page/store.html', context)

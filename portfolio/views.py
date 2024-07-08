from django.shortcuts import render

def home(request):
    return render(request, 'portfolio-page/portfolio.html')
def contact(request):
    return render(request, 'contact-page/contact.html')
def error(request):
    return render(request, '404error-page/404.html')

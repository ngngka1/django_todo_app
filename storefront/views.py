from django.shortcuts import render

def show_home_page(request):
    return render(request, 'index.html')

def show_about_page(request):
    return render(request, 'about.html')
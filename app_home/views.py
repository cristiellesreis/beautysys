from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing_page/landing_page.html')

@login_required
def home(request):
    return render(request, 'dashboard/dashboard.html')

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.

def home(request):
  return render(request, 'home.html')

def register_user(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    if not name or not email:
      return render(request, 'register_user.html', {'error': 'Todos os campos são obrigatórios'})
    try:
      user = User(name=name, email=email, phone_number=phone_number)
      user.save()
      return redirect(reverse('home'))  # Use o nome da view aqui
    except Exception as e:
      # Capturar o erro e renderizar a página com uma mensagem de erro
      return render(request, 'register_user.html', {'error': str(e)})
  return render(request, 'register_user.html')
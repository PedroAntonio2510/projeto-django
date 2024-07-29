from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.

def home(request):
  return render(request, 'home.html')

def register_user(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    image = request.FILES.get('image')
    if not name or not email:
      return render(request, 'register_user.html', {'error': 'Todos os campos são obrigatórios'})
    try:
      user = User(name=name, email=email, phone_number=phone_number, image=image)
      user.save()
      return redirect(reverse('home'))  # Use o nome da view aqui
    except Exception as e:
      # Capturar o erro e renderizar a página com uma mensagem de erro
      return render(request, 'register_user.html', {'error': str(e)})
  return render(request, 'register_user.html')

def user_login(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    user = authenticate(request)
    if user is not None:
      login(request, user)
      return redirect(reverse('home', id=id))
    else:
      messages.error(request, 'Email não encontrado.')
  return render(request, 'login.html', {'message': 'Usuário ou senha inválidos'})


@login_required
def profile_user(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'profile.html', {'user': user})

def logout(request):
  logout(request)
  return redirect(reverse('home'))
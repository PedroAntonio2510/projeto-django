from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.utils import timezone
from .models import Product

# Create your views here.

def home(request):
    if request.method == 'POST':
        if 'edit_product' in request.POST:
            # Editar produto
            id = request.POST.get('id')
            name = request.POST.get('name')
            code = request.POST.get('code')
            price = request.POST.get('price')
            
            if id and name and code and price:
                product = get_object_or_404(Product, id=id)
                product.name = name
                product.code = code
                product.price = price
                product.save()
            return redirect('home')
        
        # Criar novo produto
        name = request.POST.get('name')
        code = request.POST.get('code')
        price = request.POST.get('price')
        
        if name and code and price:
            try:
                Product.objects.create(name=name, code=code, price=price)
            except Exception as e:
                return render(request, 'home.html', {'error': str(e)})
            return redirect('home')
    
    today = timezone.now().date()
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def delete_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id:
            product = get_object_or_404(Product, id=id)
            product.delete()
    return redirect('home')


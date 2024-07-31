from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('delete/', views.delete_product, name='delete_product'),
]

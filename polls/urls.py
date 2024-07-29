from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name='home'),  # Home page
    path("register/", views.register_user, name='register_user'),
    path('login/', views.user_login, name='login'),
    path("profile/<int:id>/", views.profile_user, name='profile'),
    path("logout/", views.logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
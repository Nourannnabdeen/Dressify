from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserProfileView, RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),  # Use the class-based view
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
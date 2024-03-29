from django.urls import path
from .views import CustomSignOutView, CustomSignInView, UserSignUp, welcome_page, CustomTemplateView, PersonProfileView

urlpatterns = [
    path('profile/<int:pk>/', PersonProfileView.as_view(), name='profile'),
    path('settings/', CustomTemplateView.as_view(), name='settings'),
    path('sign-up/', UserSignUp.as_view(), name='register'),
    path('sign-out/', CustomSignOutView.as_view(), name='logout'),
    path('sign-in/', CustomSignInView.as_view(), name='login'),
    path('welcome-page/', welcome_page, name='welcome-page')
]

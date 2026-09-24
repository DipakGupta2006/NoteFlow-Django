from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),

     # 1. Email mangne wala page
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    
    # 2. "Email bhej diya gaya hai" wala success page
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    
    # 3. Email wale link par click karne ke baad naya password dalne wala page
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    
    # 4. "Password successfully change ho gaya" wala page
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    path("", views.landing_view, name="landing"),
    
]
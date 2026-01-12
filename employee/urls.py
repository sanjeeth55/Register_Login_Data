from django.urls import path
from . views import login_view, logout_view, register, about, home, features, contact

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('about/', about, name='about'),
    path('features/', features, name='features'),
    path('contact/', contact, name='contact'),
]

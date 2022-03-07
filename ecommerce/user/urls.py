from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='user_home'),
    path('about/', about, name='user_about'),
    path('contact/', contact, name='user_contact_two'),
    path('seed-user/', seed_user, name='user_seed_user'),
]
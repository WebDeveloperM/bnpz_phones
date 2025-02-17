from django.urls import path
from . import views

urlpatterns = [
    path('', views.phones, name='home'),
    # path('phones/', views.phones, name='phones'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
]
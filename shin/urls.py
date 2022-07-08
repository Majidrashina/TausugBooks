from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shin'

urlpatterns = [
    path('',views.Homepage, name="homepage"),   
    path('buybooks/',views.Books, name="buybooks"),
    path('order/',views.Checkout, name="order"),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('edit/<int:id>', views.edit, name='edit'),
]

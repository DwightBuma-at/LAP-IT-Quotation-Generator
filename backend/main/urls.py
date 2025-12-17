from django.urls import path
from . import views

urlpatterns = [
    path('create-quotation/', views.create_quotation, name='create_quotation'),
]

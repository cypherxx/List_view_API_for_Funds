from django.contrib import admin
from django.urls import path,include
from .views import Fund_view,Funds_view

urlpatterns = [
    path('funds/',Funds_view),
    path('funds/<str:nm>',Fund_view),
]

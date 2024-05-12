from django.urls import path
from . import views

urlpatterns = [
    path('teknik/', views.TeknikListCreate.as_view(), name="Teknik-view-create"),
    path('teknik/<int:pk>/', views.TeknikRetrieveUpdateDestory.as_view(), name=""),
    path('computer/', views.ComputerListCreate.as_view(), name="Computer-view-create"),
    path('computer/<int:pk>/', views.ComputerRetrieveUpdateDestory.as_view(), name=""),
    path('elit/', views.ElitListCreate.as_view(), name="Elit-view-create"),
    path('elit/<int:pk>/', views.ElitRetrieveUpdateDestory.as_view(), name=""),
]
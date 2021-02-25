from django.urls import path
from .import views 

urlpatterns = [
    path('getPizzas/', views.GetPizzas.as_view()),
    path('createPizzas/', views.CreatePizzas.as_view()),
    path('updateOrDelete/<str:pk>/', views.UpdateOrDelete.as_view()),
    path('filterPizza/', views.FilterPizza.as_view()),

    path('addSize/', views.AddSize.as_view()),
    path('addTopping/', views.AddTopping.as_view()),
    path('getSize/', views.GetSize.as_view()),
    path('getTopping/', views.GetTopping.as_view()),
]
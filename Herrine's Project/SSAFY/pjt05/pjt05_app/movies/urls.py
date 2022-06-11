from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('mainboard/', views.mainboard, name='mainboard'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),    
    path('index/', views.index, name='index'),
    path('recommendation/', views.recommendation, name='recommendation'),
]
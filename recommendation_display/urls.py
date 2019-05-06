from django.urls import path
from . import views

urlpatterns = [
                path('', views.index_view ), 
                path('user/', views.recommendation_display_view), 
                
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('details-new/<int:pk>/', views.detail_new, name='detail-new'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('added/', views.added, name='added'),
    path('add-movie/<slug:slug>', views.add_movie, name='add-movie'),
    path('deleting-added/<slug:slug>', views.deleting_added, name='deleting-added'),
]
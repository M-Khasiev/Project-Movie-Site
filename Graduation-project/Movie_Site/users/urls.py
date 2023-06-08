from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('added/', views.added, name='added'),
    path('account-settings/', views.account_settings, name='account-settings'),
    path('account-delete/', views.account_delete, name='account-delete'),
    path('add-movie/<slug:slug>', views.add_movie, name='add-movie'),
    path('deleting-added/<slug:slug>', views.deleting_added, name='deleting-added'),
    path('review-delete/<slug:slug>/', views.review_delete, name='review-delete'),
]

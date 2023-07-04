from django.urls import path
from . import views

urlpatterns = [
    # Регистрация
    path('registration/', views.registration, name='registration'),
    # Авторизация
    path('login/', views.login_user, name='login'),
    # Выход из аккаунта
    path('logout/', views.logout_user, name='logout'),
    # Добавленные фильмы в раздел 'Мои фильмы'
    path('added/', views.added, name='added'),
    # Настройки аккаунта
    path('account-settings/', views.account_settings, name='account-settings'),
    # Удаление аккаунта
    path('account-delete/', views.account_delete, name='account-delete'),
    # Добавление фильма в раздел 'Мои фильмы'
    path('add-movie/<slug:slug>', views.add_movie, name='add-movie'),
    # Удаление фильма из раздела 'Мои фильмы'
    path('deleting-added/<slug:slug>', views.deleting_added, name='deleting-added'),
    # Удаление отзыва к фильму
    path('review-delete/<slug:slug>/', views.review_delete, name='review-delete'),
    # Удаление отзыва к новости
    path('news-review-delete/<int:pk>/', views.news_review_delete, name='news-review-delete'),
    # Удаление вопроса из форума
    path('forum-question-delete/<int:pk>/', views.forum_question_delete, name='forum-question-delete'),
    # Удаление отзыва к вопросу на форуме
    path('forum-review-question-delete/<int:pk>/', views.forum_review_question_delete,
         name='forum-review-question-delete'),
]

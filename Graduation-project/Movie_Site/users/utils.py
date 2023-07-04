from home.models import Movie, Review
from news.models import ReviewNews
from forum.models import QuestionUser, ReviewQuestion


def user_movies(request):
    """Фильмы пользователя, добавленные в 'Мои фильмы'"""
    movies = list()
    for i in Movie.objects.all():
        for j in i.adding_movie.all():
            if request.user.username == str(j):
                movies.append(i)
    return movies


def is_there_review_movie(request):
    """Наличие отзывов к фильмам"""
    review = Review.objects.filter(owner_id=request.user.id)
    if review:
        return True
    else:
        return False


def is_there_review_news(request):
    """Наличие отзывов к новостям"""
    review = ReviewNews.objects.filter(owner_id=request.user.id)
    if review:
        return True
    else:
        return False


def is_there_questions(request):
    """Наличие вопросов пользователя на форуме"""
    question = QuestionUser.objects.filter(user_id=request.user.id)
    if question:
        return True
    else:
        return False


def is_there_questions_review(request):
    """Наличие отзывов к вопросам на форуме"""
    question_review = ReviewQuestion.objects.filter(owner_id=request.user.id)
    if question_review:
        return True
    else:
        return False

from home.models import Movie


def user_movies(request):
    movies = list()
    for i in Movie.objects.all():
        for j in i.adding_movie.all():
            if request.user.username == str(j):
                movies.append(i)
    return movies

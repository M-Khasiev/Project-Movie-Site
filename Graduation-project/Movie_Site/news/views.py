from django.shortcuts import render, redirect
from .models import News
from home.models import Movie
from .forms import ReviewNewForm
from django.contrib import messages
from .utils import parser, paginate_news, true_body_news


def news(request):
    """Вывод новостей"""
    # parser()
    last_added = Movie.objects.order_by('-pk')[:5]
    news_site = News.objects.all()
    custom_range, news_site = paginate_news(request, news_site, 20)
    context = {'news': news_site,
               'last_added': last_added,
               'custom_range': custom_range}
    return render(request, 'news/news.html', context)


def detail_new(request, pk):
    """Детальное описание новости"""
    last_added = Movie.objects.order_by('-pk')[:5]
    new_detail = News.objects.get(id=pk)
    review_body_check = true_body_news(pk)
    form = ReviewNewForm()

    if request.method == 'POST':
        form = ReviewNewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.news = new_detail
            review.owner = request.user
            review.save()

            messages.success(request, 'Ваш отзыв успешно отправлен!')
            return redirect(request.META.get('HTTP_REFERER'))

    context = {'news': new_detail,
               'last_added': last_added,
               'form': form,
               'review_body_check': review_body_check
               }
    return render(request, 'news/detail_new.html', context)

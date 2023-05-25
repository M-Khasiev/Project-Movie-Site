from django.shortcuts import render
from .models import News
from home.models import Movie
from .utils import parser, paginate_news


def news(request):
    # parser()
    last_added = Movie.objects.order_by('-pk')[:5]
    news_site = News.objects.all()
    custom_range, news_site = paginate_news(request, news_site, 6)
    context = {'news': news_site,
               'last_added': last_added,
               'custom_range': custom_range}
    return render(request, 'news/news.html', context)


def detail_new(request, pk):
    last_added = Movie.objects.order_by('-pk')[:5]
    new_detail = News.objects.get(id=pk)
    context = {'news': new_detail,
               'last_added': last_added
               }
    return render(request, 'news/detail_new.html', context)

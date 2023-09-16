import requests
from .models import News
from bs4 import BeautifulSoup as BS
from django.core.paginator import Paginator


def parser():
    """Парсер для получения новостей"""
    url_image_new = ''
    description_new = ''
    res = 0
    for i in range(1):
        url = f'https://lenta.ru/rubrics/culture/kino/{i}/'
        page = requests.get(url)
        html = BS(page.content, 'html.parser')

        for el in html.find_all(class_="rubric-page__item")[:-1]:
            title_new = el.h3.text
            url_2 = f"https://lenta.ru/{el.a.get('href')}"
            page_2 = requests.get(url_2)
            html_2 = BS(page_2.content, 'html.parser')

            for j in html_2.find_all('div', class_='picture__image-wrap'):
                url_image_new = j.img.get('src')

            for k in html_2.find_all('div', class_='topic-body__content'):
                description_new = k.text
            for i in News.objects.all():
                if i.title == title_new:
                    res += 1
            if res == 0:
                News.objects.create(title=title_new,
                                    url_image=url_image_new,
                                    description=description_new
                                    )
            else:
                continue
            res = 0
            url_image_new = ''


def paginate_news(request, news, results):
    """Пагинация на странице с новостями"""
    page = request.GET.get('page', 1)
    # results = 6
    paginator = Paginator(news, results, allow_empty_first_page=False)

    news = paginator.get_page(page)

    left_index = int(page) - 2

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 3

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, news


def true_body_news(pk):
    """Наличие отзывов"""
    news_detail = News.objects.get(id=pk)
    res = 0
    for review in news_detail.reviewnews_set.all():
        if review.body:
            res += 1
    return res

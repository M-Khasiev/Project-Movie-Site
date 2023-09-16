from django.core.paginator import Paginator
from .models import ReviewQuestion, QuestionUser


def paginate_questions(request, questions, results):
    """Пагинация на странице с вопросами"""
    page = request.GET.get('page', 1)
    # results = 6
    paginator = Paginator(questions, results, allow_empty_first_page=False)

    questions = paginator.get_page(page)

    left_index = int(page) - 2

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 3

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, questions


def true_body_question(pk):
    """Наличие отзывов"""
    question_detail = QuestionUser.objects.get(id=pk)
    res = 0
    for review in question_detail.reviewquestion_set.all():
        if review.body:
            res += 1
    return res

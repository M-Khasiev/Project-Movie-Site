from django.shortcuts import render, redirect
from .forms import ForumAskQuestion, ReviewQuestionForm
from django.contrib import messages
from .models import QuestionUser
from django.core.paginator import EmptyPage
from django.db.models import Q
from .utils import paginate_questions, true_body_question


def forum(request):
    questions = QuestionUser.objects.all()
    try:
        custom_range, questions = paginate_questions(request, questions, 10)
    except EmptyPage:
        return render(request, 'forum/forum_questions.html', {'error': 'Ничего не найдено'})
    context = {
        'questions': questions,
        'custom_range': custom_range
    }
    return render(request, 'forum/forum_questions.html', context)


def forum_ask_question(request):
    if request.user.is_authenticated:
        form = ForumAskQuestion()
        context = {
            'form': form,
        }
        return render(request, 'forum/forum_ask_question.html', context)
    else:
        return redirect('login')


def save_question(request):
    if request.method == 'POST':
        form = ForumAskQuestion(request.POST)
        if form.is_valid():
            question_form = form.save(commit=False)
            question_form.user = request.user
            question_form.save()
            messages.success(request, 'Ваш вопрос успешно отправлен!')
            return redirect('forum')
        else:
            messages.error(request, form.errors)
            return redirect(request.META.get('HTTP_REFERER'))


def detail_question(request, pk):
    question = QuestionUser.objects.get(id=pk)
    review_body_check = true_body_question(pk)
    form = ReviewQuestionForm()

    if request.method == 'POST':
        form = ReviewQuestionForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.question_user = question
            review.owner = request.user
            review.save()

            messages.success(request, 'Ваш отзыв успешно отправлен!')
            return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'question': question,
        'form': form,
        'review_body_check': review_body_check,
    }
    return render(request, 'forum/detail_question.html', context)


def search_question(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    url_search_query = f"search_query={request.GET.get('search_query')}&"
    questions = QuestionUser.objects.distinct().filter(Q(user__username__iregex=search_query) |
                                                       Q(subject__iregex=search_query))
    try:
        custom_range, questions = paginate_questions(request, questions, 6)
    except EmptyPage:
        return render(request, 'forum/forum_questions.html', {'error': 'Ничего не найдено'})
    context = {'questions': questions,
               'custom_range': custom_range,
               'search': url_search_query
               }
    return render(request, 'forum/forum_questions.html', context)

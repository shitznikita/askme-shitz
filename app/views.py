import copy

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

QUESTIONS = [
    {
        'title': 'Title ' + str(i),
        'id': i,
        'text': 'Text ' + str(i)
    } for i in range(30)
]

def paginate(object_list, request, per_page=10):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(object_list, per_page)
    page = paginator.page(page_num)
    return page

def index(request):
    page = paginate(QUESTIONS, request, 5)
    return render(request, template_name='index.html', context={
        'questions': page.object_list, 'page_obj': page
    })

def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()

    page = paginate(hot_questions, request, 5)

    return render(request, template_name='hot_questions.html', context={
        'questions': page.object_list, 'page_obj': page
    })

def ask(request):
    return render(request, template_name='ask.html')

def one_question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(request, template_name='one_question.html', context={
        'item': one_question
    })

def login(request):
    return render(request, template_name='login.html')

def signup(request):
    return render(request, template_name='signup.html')

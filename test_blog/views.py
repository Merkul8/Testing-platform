from django.shortcuts import redirect, render
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import Group



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'test_blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            admin_group ,c = Group.objects.get_or_create(name='Администраторы')
            user.groups.add(admin_group)
            messages.success(request, 'Успешная регистрация')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'test_blog/register.html', {'form': form})


def main(request):
    tests = Tests.objects.all()
    return render(request, 'test_blog/main.html', {'tests': tests})


class Test(ListView):
    model = Question
    context_object_name = 'test'
    template_name = 'test_blog/test.html'
    # я знаю про paginate_by, но почему то с ним ничего не получалось


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(test__slug=self.kwargs['slug'])
        questions_per_page = 1
        
        paginator = Paginator(questions, questions_per_page)
        page_number = self.request.GET.get('page')
        page = paginator.get_page(page_number)
        context['answers'] = Answers.objects.all()
        context['questions'] = page
        return context
    
    # def post(self, **kwargs):
    #     questions = Answers.objects.all()
    #     for question in questions



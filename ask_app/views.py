from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.core.paginator import Paginator
from ask_app.models import *
from ask_app.forms import *
from django.shortcuts import redirect
from django.contrib import auth


# Create your views here.
@csrf_exempt
def application(request):
    
    output = 'Django'

    output += 'Post:'
    output+= '<form method="post">'
    output+= '<input type="text" name = "test">'
    output+= '<input type="submit" value="Send">'
    output+= '</form>'
    if request.method == 'GET':
        getItems = request.GET

        for item in getItems:
    	    output += getItems[item]
    	    output += '<br>'

    if request.method == 'POST':
        postItems = request.POST

        for item in postItems:
    	    output += postItems[item]
    	    output += '<br>'

    return HttpResponse(output)

members = []
members_shablon = ["Dr. House", "Queen Victoria", "Harry Potter"]
for i in range(1, 8):
	members.append(members_shablon[i / len(members_shablon)])

popular_tags = []
popular_tags_shablon = ["Python", "Mail.ru", "SQL"]
for i in range(1, 8):
	popular_tags.append({'name': str(i) * 3,})

def lists(list_objects, page_number):
    paginator = Paginator(list_objects, 5)
    try:
        page = paginator.page(page_number)
    except:
        page = paginator.page(paginator.num_pages)
    return page

def index(request, page_number = 1):
    if len(request.GET) > 0:
        page_number= (int(request.GET['question_id']) - 1) / 5 + 1
    page_questions = lists(Question.objects.new(), page_number)
    if int(page_number) != int(page_questions.number):
        return redirect('index', page_number=page_questions.number) 
    #author = Author.objects.
    return render(request, 'index.html', {'page': page_questions, 'members': members, 'popular_tags': popular_tags})

def hot(request, page_number = 1):
    page_questions = lists(Question.objects.hot(), page_number)
    if int(page_number) != int(page_questions.number):
        return redirect('hot', page_number=page_questions.number)
    return render(request, 'hot.html', {'page': page_questions,  'members': members, 'popular_tags': popular_tags})

def signup(request):
    
    if request.POST:
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.add()
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            auth.login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', { 'members': members, 'popular_tags': popular_tags, 'form': form})

def ask(request):
    if not request.user.is_authenticated():
        return redirect('/login/?continue=/ask/')
    if request.POST:
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.add(request.user)
            return redirect('/question/' + str(question.id))
    else:
        form = AskForm()
	return render(request, 'ask.html', { 'members': members, 'popular_tags': popular_tags, 'form': form})

def login(request):
    contin = request.GET.get('continue')
    
    print(contin)

    if contin is None:
        contin = '/'

    print(contin)

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            # auth.logout(request)
            # user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            auth.login(request, form.user)
            if len(request.GET) > 0:
                return redirect(request.GET['continue'])
            
                return redirect(contin)
            return redirect('/')  
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'members': members, 'popular_tags': popular_tags, 'form': form})

def logout(request):
    auth.logout(request)
    if len(request.GET) > 0:
        return redirect(request.GET['continue'])
    return redirect('/')

def tag(request, tag_name, page_number = 1):

    questions_with_tag = Question.objects.tag(tag_name)
    page_questions = lists(questions_with_tag, page_number)
    if int(page_number) != int(page_questions.number):
        return redirect('tag', tag_name=tag_name ,page_number=page_questions.number)
    return render(request, 'tag.html', {'page': page_questions, 'using_tag': tag_name, 'members': members, 'popular_tags': popular_tags})

def question(request, question_number, page_number = 1):
    if request.POST:
        if not request.user.is_authenticated():
            return redirect('/login/?continue=/question/'+str(question_number)+'/'+str(page_number))
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer=form.add(request.user, question_number)
            return redirect('/question/'+str(question_number)+'/'+str(page_number)+'/?answer_id='+str(answer.id)+'#'+str(answer.id))
    else:
        form = AnswerForm()
        using_question = Question.objects.number(question_number)
        answers = Answer.objects.question(question_number)
        if len(request.GET) > 0:
            page_number= (int(request.GET['answer_id']) - 1) / 5 + 1
        page_answers = lists(answers, page_number)
        if int(page_number) != int(page_answers.number):
            return redirect('question', question_number=question_number ,page_number=page_answers.number)
    return render(request, 'question.html', {'page': page_answers, 'using_question': using_question,  'members': members, 'popular_tags': popular_tags, 'form': form})

def setting(request):
    

    if not request.user.is_authenticated():
        return redirect('/login?continue=/setting')
    author = request.user.author
    if request.POST:
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.add(request.user)
            form = SettingsForm(initial={'username': author.username, 'hid_username': author.username, 'email': author.email, 'hid_email': request.user.email, 'password': request.user.password, 'repeat_password': request.user.password})
            # return redirect('/setting/')
        return render(request, 'setting.html', {'members': members, 'popular_tags': popular_tags, 'form': form})
    else:
        author = Author.objects.get(username=request.user.username)
        form = SettingsForm(initial={'username': author.username, 'hid_username': author.username, 'email': author.email, 'hid_email': request.user.email, 'password': request.user.password, 'repeat_password': request.user.password})
        return render(request, 'setting.html', {'members': members, 'popular_tags': popular_tags, 'form': form})

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.core.paginator import Paginator

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

questions = []
for i in range(1, 25):
  	questions.append({
   		'number': str(i),
   		'title': 'title ' + str(i),
   		'text': "Bootstrap is downloadable in two forms, within which you'll find the following directories and files",
   		'tags': [str(i) * 3, str(i + 1) * 3, str(i + 2) * 3, str(i + 3) * 3, str(i + 4) * 3, str(i + 5) * 3],
        'likes': random.randint(1, 28),
   	})

answers = []
for i in range(1, 25):
	answers.append({
        'text': "Bootstrap is downloadable in two forms, within which you'll find the following directories and files",
        'likes': random.randint(1, 28),
	})

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
	page = paginator.page(page_number)
	return page

def index(request, page_number = 1):
	page_questions = lists(questions, page_number)
	return render(request, 'index.html', {'page': page_questions, 'members': members, 'popular_tags': popular_tags})

def hot(request, page_number = 1):
	page_questions = lists(questions, page_number)
	return render(request, 'hot.html', {'page': page_questions,  'members': members, 'popular_tags': popular_tags})

def signup(request):
	return render(request, 'signup.html', { 'members': members, 'popular_tags': popular_tags})

def ask(request):
	return render(request, 'ask.html', { 'members': members, 'popular_tags': popular_tags})

def login(request):
	return render(request, 'login.html', { 'members': members, 'popular_tags': popular_tags})

def tag(request, tag_name, page_number = 1):
    questions_with_tag = []
    for i in questions:
        if tag_name in i['tags']:
            questions_with_tag.append(i)
    page_questions = lists(questions_with_tag, page_number)
    return render(request, 'tag.html', {'page': page_questions, 'using_tag': tag_name, 'members': members, 'popular_tags': popular_tags})

def question(request, question_number, page_number = 1):
	using_question = dict()
	for question in questions:
		if str(question['number']) == question_number:
			using_question = question
	page_answers = lists(answers, page_number)

	return render(request, 'question.html', {'page': page_answers, 'using_question': using_question,  'members': members, 'popular_tags': popular_tags})

def setting(request):
	return render(request, 'setting.html', {'members': members, 'popular_tags': popular_tags})

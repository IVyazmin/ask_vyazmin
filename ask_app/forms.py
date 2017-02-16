from django import forms
from ask_app.models import *
from django.core import validators
from django.contrib import auth

class SignupForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter username"}))
	email = forms.EmailField(label='Email', max_length=20, widget=forms.EmailInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter email"}))
	repeat_password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter password"}))
	password = forms.CharField(label='Repeat password', max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'placeholder': "Repeat password"}))
	image = forms.ImageField(label='Loud avatar', required=False, widget=forms.FileInput(attrs={'class': 'form-control input-lg'}))
	def clean_username(self):
		new_name = self.cleaned_data['username']
		for user in Author.objects.all():
			if user.username == new_name:
				raise forms.ValidationError("Username is already exist")
				break
		return new_name

	def clean_email(self):
		new_email = self.cleaned_data['email']
		for user in Author.objects.all():
			if user.email == new_email:
				raise forms.ValidationError("Email is already exist")
				break
		return new_email

	def clean_password(self):
		if self.cleaned_data['repeat_password'] != self.cleaned_data['password']:
			raise forms.ValidationError("Different passwords")
		return self.cleaned_data['password']

	def add(self):
		Author.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'], image=self.cleaned_data['image'])

class SearchForm(forms.Form):
	text_search = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control col-md-5'}))

class AskForm(forms.Form):
	title = forms.CharField(label='Title', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter title"}))
	text = forms.CharField(label='Text', max_length=256, widget=forms.Textarea(attrs={'class': 'form-control input-lg', 'rows': 20, 'placeholder': "Enter text"}))
	tags = forms.CharField(label='Tags', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter tags"}))

	def add(self, _author):
		_author = Author.objects.get(id=_author.id)
		question = Question(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=_author)
		question.save()
		tags = self.cleaned_data['tags'].split(',')
		for new_tag in tags:
			tag = Tag.objects.filter(name=new_tag)
			if len(tag) == 0:
				tag = Tag(name=new_tag)
				tag.save()
			else:
				tag = tag[0]
			question.tags.add(tag)
		question.save()		
		return question

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter username"}))
	password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter password", }))

	def clean(self):
		# raise forms.ValidationError("Wrong login or password")
		self.user = auth.authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if self.user is  None:
			raise forms.ValidationError("Wrong login or password")
		if not self.user.is_active:
			raise forms.ValidationError("Wrong login or password")
		return self.cleaned_data['password']


class AnswerForm(forms.Form):
	text = forms.CharField(label='Your answer', max_length=256, widget=forms.Textarea(attrs={'class': 'form-control input-lg', 'rows': 8, 'placeholder': "Enter text"}))

	def add(self, _author, question_number):
		_author = Author.objects.get(id=_author.id)
		_question = Question.objects.number(question_number)
		answer = Answer(text=self.cleaned_data['text'], author=_author, question=_question)
		answer.save()
		return answer

class SettingsForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter username"}))
	email = forms.EmailField(label='Email', max_length=20, widget=forms.EmailInput(attrs={'class': 'form-control input-lg', 'placeholder': "Enter email"}))
	image = forms.ImageField(label='Loud avatar', required=False, widget=forms.FileInput(attrs={'class': 'form-control input-lg'}))
#	def clean_username(self):
#		new_name = self.cleaned_data['username']
#		for user in Author.objects.all():
#			if user.username == new_name:
#				if str(new_name) != str(self.fields['hid_username']):
#					raise forms.ValidationError("Username is already exist")
#					break
#		return new_name
#
#	def clean_email(self):
#		new_email = self.cleaned_data['email']
#		for user in Author.objects.all():
#			if user.email == new_email:
#				if str(new_email) != str(self.fields['hid_email']) :	
#					raise forms.ValidationError("Email is already exist")
#					break
#		return new_email


	def add(self, _author):
		author = Author.objects.get(id=_author.id)
		author.username = self.cleaned_data['username']
		author.email = self.cleaned_data['email']
		author.image = self.cleaned_data['image']
		#print (author.email)
		author.save()

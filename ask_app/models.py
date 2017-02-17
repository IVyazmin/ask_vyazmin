# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class AnswerManager(models.Manager):

	def correct(self):
		return self.filter(is_correct=True)

	def question(self, question_id):
		return self.filter(question=question_id)

class QuestionManager(models.Manager):

	def hot(self):
		return self.order_by("-time_add")

	def new(self):
		return self.order_by("-likes")

	def tag(self, tag_name):
		return get_list_or_404(self, tags__name=tag_name)

	def number(self, question_id):
		return get_object_or_404(self, id=question_id)


class Answer(models.Model):
	text = models.TextField(verbose_name=u'Текст')
	is_correct = models.TextField( verbose_name=u'Правильный', default='')
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	likes = models.IntegerField(verbose_name=u'Лайк', default=0)
	

	objects = AnswerManager()

	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name = u'Ответ'
		verbose_name_plural = u'Ответы'

class Question(models.Model):
	time_add = models.DateTimeField(verbose_name=u'Время добавления', auto_now_add=True)
	title = models.CharField(max_length=255, verbose_name=u'Заголовок')
	text = models.TextField(verbose_name=u'Текст')
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	tags = models.ManyToManyField('Tag')
	likes = models.IntegerField(verbose_name=u'Лайк', default=0)
	answers = models.IntegerField(verbose_name=u'Количество ответов', default=0)
	
	
	objects = QuestionManager()

	def count_likes(self):
		self.likes = self.likequestion_set.all().count()
		self.save()

	def count_answers(self):
		self.answers = self.answer_set.all().count()
		self.save()

	class Meta:
		verbose_name = u'Вопрос'
		verbose_name_plural = u'Вопросы'

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=10, verbose_name=u'Тэг')
	
	class Meta:
		verbose_name = u'Тэг'
		verbose_name_plural = u'Тэги'

	def __unicode__(self):
		return self.name

class Author(User):
	publications = models.IntegerField(verbose_name=u'Публикации', default=0)
	image = models.ImageField(verbose_name=u'Аватар', upload_to='')
	#objects = AuthorManager()
	
	class Meta:
		verbose_name = u'Автор'
		verbose_name_plural =u'Авторы'

	def __unicode__(self):
		return self.username

class LikeQuestion(models.Model):
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	status = models.IntegerField(verbose_name=u'Статус', default=0)

	class Meta:
		verbose_name = u'Лайк вопросу'
		verbose_name_plural = u'Лайки вопросу'

class LikeAnswer(models.Model):
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
	status = models.IntegerField(verbose_name=u'Статус', default=0)

	class Meta:
		verbose_name = u'Лайк ответу'
		verbose_name_plural = u'Лайки ответу'
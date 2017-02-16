from django.core.management.base import BaseCommand, CommandError
from ask_app.models import *
import random

class Command(BaseCommand):

	def fill_tags(self):
		for i in range(0, 20):
			_name = ''
			for j in range(0, 5):
				_name += random.choice('qwertyuiopasdfghjk')
			_tag = Tag(name=_name)
			_tag.save()

	def fill_authors(self):
		list_autors_name = ['Pushkin',' Tolstoy', 'Gogol', 'Dostoevskiy', 'Solovyev', 'Kluchevskiy', 'Chehov', 'Nekrasov', 'Goncharov', 'Radishev', 'Sholohov']
		list_images = ['../static/r.jpg', '../static/list.png', '../static/fire.jpg', '../static/water.jpg', '../static/heart.png']
		for name in list_autors_name:
			image = random.choice(list_images)
			Author.objects.create_user(username=name, password=777)

	def fill_questions(self):
		for i in range(0, 20):
			_title = ''
			_text = ''
			for j in range(0, 12):
				_title += random.choice('qwertyuiopasdfghjk')
				word = ''
				for t in range(0, 5):
					word += random.choice('qwertyuiopasdfghjk')
				_text += word
			_author=random.choice(Author.objects.all())
			_question = Question(title=_title, text=_text, author=_author)
			_question.save()
			for i in range(1, 4):
				_tag = random.choice(Tag.objects.all())
				_question.tags.add(_tag)
			_question.save()

	def fill_answers(self):
		for i in range(0, 100):
			_text = ''
			for j in range(0, 12):
				word = ''
				for t in range(0, 5):
					word += random.choice('qwertyuiopasdfghjk')
				_text += word
			correct = random.choice([False, True])
			_author=random.choice(Author.objects.all())
			_question=random.choice(Question.objects.all())
			_answer = Answer(text=_text, is_correct=correct, author=_author, question=_question)
			_answer.save()

	def fill_likes_questions(self):
		for i in range (0, 100):
			_author=random.choice(Author.objects.all())
			_question=random.choice(Question.objects.all())
			_likeQuestion = LikeQuestion(author=_author, question=_question)
			_likeQuestion.save()

	def fill_likes_answers(self):
		for i in range (0, 500):
			_author=random.choice(Author.objects.all())
			_answer=random.choice(Answer.objects.all())
			_likeAnswer = LikeAnswer(author=_author, answer=_answer)
			_likeAnswer.save()


	def handle(self, *args, **options):
		self.fill_tags()
		self.fill_authors()
		self.fill_questions()
		self.fill_answers()
		self.fill_likes_questions()
		self.fill_likes_answers()
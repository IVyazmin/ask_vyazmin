from django.contrib import admin
from ask_app import models
from django.contrib.auth.models import User, UserManager

class QuestionAdmin(admin.ModelAdmin):
	list_display=('title',)

class AuthorAdmin(admin.ModelAdmin):
	list_display=('username',)

class TagAdmin(admin.ModelAdmin):
	list_display=('name',)

class AnswerAdmin(admin.ModelAdmin):
	list_display=('text',)

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Answer, AnswerAdmin)
from django.contrib import admin
from .models import Tests, Question, Answers
from django.contrib.auth.models import User


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'true_or_false', 'question')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'test')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tests, TestsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswersAdmin)

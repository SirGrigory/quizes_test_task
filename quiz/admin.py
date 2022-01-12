from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Quiz, Question, Answer, Choice


class ChoiceInLine(NestedStackedInline):
    model = Choice
    extra = 0

class QuestionInLine(NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInLine]
    
@admin.register(Quiz)
class QuizAdmin(NestedModelAdmin):
    list_display = ('id', 'title', 'start_date','end_date', 'description')
    list_display_links = ('title',)
    save_on_top = True
    fieldsets = (
        ('Main', {
            'fields': ('title', 'description')
            }),
        ('Dates', {
            'fields': (('start_date', 'end_date'), )
            }),
    )
    inlines = [QuestionInLine]

    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ['start_date']
        else:
            return []

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('id','q_type', 'text','quiz')
#     # inlines = [ChoiceInLine]
    
# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'question', 'text')


# admin.site.register(Answer)

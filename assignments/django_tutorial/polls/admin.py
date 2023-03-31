from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """Make the data align itself in a row"""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # choose which database columns to use to order results
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # same but with filtering -- pub_date is a database column
    list_filter = ['pub_date']
    # search field for looking up questions via the question_text column
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

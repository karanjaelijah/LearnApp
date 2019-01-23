from django.contrib import admin
from  .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fieds': ['qustion_text']}),
        ('Date information',  {'felds': ['pub_date']}),
['collapse']}),
    ]
    inlines = [ChoiceInline]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
admin.site.register(Question, QuestionAdmin)



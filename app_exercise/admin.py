from django.contrib import admin
from app_exercise.models import exam

# Register your models here.

@admin.register(exam)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['ref_id','problem_text','choice1','choice2','choice3','choice4']


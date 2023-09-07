from django.contrib import admin
from .models import exercises ,shortnote

# Register your models here.

@admin.register(exercises)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'title', 'subject', 'max_problem', 'perround_problem']

@admin.register(shortnote)
class ShortnoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'subject', 'time_stamp']
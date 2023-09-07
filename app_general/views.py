from django.shortcuts import render
from django.http import HttpResponse
from .models import exercises , shortnote ,shortnote_page
from app_exercise.models import exercise_result , result , exam
from django.db.models import Avg,Sum
from django.contrib.auth.models import User

# More Function

from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None

# Create your views here.

all_exercises = exercises.objects.order_by('id') 

def home(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched != '':
            exercises_1 = exercises.objects.filter(ref_id__icontains=searched)
            exercises_2 = exercises.objects.filter(title__icontains=searched)
            exercises_3 = exercises.objects.filter(subject__icontains=searched)
            context = { 
                'exercises_searched': list(exercises_1)+list(exercises_2)+list(exercises_3),
                'searched':searched,
            }
            return render(request ,'app_general/home.html',context)
        else:
            context = { 'exercises': all_exercises}
            return render(request ,'app_general/home.html',context)
    context = { 'exercises': all_exercises}
    return render(request ,'app_general/home.html',context)

def evaluation(request):
    lastest_result = exercise_result.objects.order_by('-doing_at').filter(user_id=User.objects.get(id=request.user.id).id)
    if request.method == "POST":
        searched = request.POST['searched']
        if searched != '':
            lastest_result_1 = exercise_result.objects.filter(ref_id__icontains=searched)
            lastest_result_2 = exercise_result.objects.filter(title__icontains=searched)
            lastest_result_3 = exercise_result.objects.filter(subject__icontains=searched)
            context = {
                'exercises': all_exercises,
                'lastest_result': list(lastest_result_1)+list(lastest_result_2)+list(lastest_result_3),
                'searched':searched,
            }
            return render(request ,'app_general/evaluation_search.html',context)
        
    context = {
        'lastest_result':lastest_result,
        'exercises':all_exercises,
    }
    return render(request,'app_general/evaluation.html',context)

def evaluation_spec(request,exam_ref_id):
    exercise = exercises.objects.get(ref_id=exam_ref_id)
    users_choose_results = exercise_result.objects.order_by('-doing_at').filter(ref_id=exam_ref_id , user_id=User.objects.get(id=request.user.id).id)
    results = result.objects.filter(user_id = User.objects.get(id=request.user.id).id)
    exams = exam.objects.filter(ref_id=exam_ref_id)

    # %
    count = exercise_result.objects.filter(ref_id=exam_ref_id,user_id=User.objects.get(id=request.user.id).id).count()
    total_point_list = exercise_result.objects.filter(ref_id=exam_ref_id , user_id=User.objects.get(id=request.user.id).id).aggregate(Sum('total_point'))
    total_sum = total_point_list['total_point__sum']
    percent = round(100*total_sum / (count * exercises.objects.get(ref_id=exam_ref_id).perround_problem ) , 2)
    

    context = {
        'exercise':exercise,
        'users_choose_results':users_choose_results,
        'results':results,
        'exam' : exams,

        'count':count,
        'percent':percent,

    }
    return render(request ,'app_general/evaluation_spec.html',context)

def shop(request):
    shortnotes = shortnote.objects.order_by('time_stamp')
    context = {
        'shortnotes':shortnotes,
    }
    return render(request,'app_general/shop.html',context)

def shopdetail(request,shortnote_id):
    a_shortnote = shortnote.objects.get(id=shortnote_id)
    context = {
        'shortnote':a_shortnote,
        'shortnote_id':shortnote_id,
    }
    return render(request,'app_general/shop-details.html',context)
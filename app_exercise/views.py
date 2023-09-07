from django.shortcuts import render ,redirect
from django.http import HttpResponse
from app_general.models import exercises
from .models import exam ,result , exercise_result
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .forms import ProductForm

# Create your views here.

@login_required
def detail_page(request,exam_ref_id):
    problems = exam.objects.all().order_by('?')
    exercise = exercises.objects.get(ref_id=exam_ref_id)
    for problem in problems:
            add_exam = exam()
            add_exam.problem_text =  problem.problem_text
            add_exam.choice1 = problem.choice1
            add_exam.choice2 = problem.choice2
            add_exam.choice3 = problem.choice3
            add_exam.choice4 = problem.choice4
            add_exam.c_id1 = problem.c_id1
            add_exam.c_id2 = problem.c_id2
            add_exam.c_id3 = problem.c_id3
            add_exam.c_id4 = problem.c_id4
            add_exam.correct_c_id = problem.correct_c_id
            add_exam.ref_id = problem.ref_id
            add_exam.solution = problem.solution
            add_exam.save()

    exam.objects.all().delete()

    for problem in problems:
            add_exam = exam()
            add_exam.problem_text =  problem.problem_text
            add_exam.choice1 = problem.choice1
            add_exam.choice2 = problem.choice2
            add_exam.choice3 = problem.choice3
            add_exam.choice4 = problem.choice4
            add_exam.c_id1 = problem.c_id1
            add_exam.c_id2 = problem.c_id2
            add_exam.c_id3 = problem.c_id3
            add_exam.c_id4 = problem.c_id4
            add_exam.correct_c_id = problem.correct_c_id
            add_exam.ref_id = problem.ref_id
            add_exam.solution = problem.solution
            add_exam.save()
    
    context = {
        'pages':pages,
        'exam_ref_id':exam_ref_id,
        'exercise':exercise,

        'problems':problems,
    }
    return render(request,'app_exercise/detail_exam.html',context)

@login_required
def pages(request,exam_ref_id,page):
    problems = exam.objects.filter(ref_id=exam_ref_id).order_by('id')
    title = exercises.objects.get(ref_id=exam_ref_id).title
    perround_problem = exercises.objects.get(ref_id=exam_ref_id).perround_problem
    user_id = User.objects.get(id=request.user.id).id

    if request.POST and int(page) ==1:
        try:
            doing = exercise_result()
            doing.ref_id = exam_ref_id
            doing.max_point = perround_problem
            doing.user_id = user_id
            doing.save()
            result.objects.get(problem_text='1_nulltext',doing_at =exercise_result.objects.order_by('-id').first().doing_at)
        except:
             for a_page in range(perround_problem):
                exam_result = result()
                exam_result.problem_text = str(a_page+1)+'_nulltext'
                exam_result.doing_at = exercise_result.objects.order_by('-id').filter(user_id=user_id).first().doing_at         #ในอนาคตเพิ่ม .filter(user_id=user_id)
                exam_result.user_id = user_id
                exam_result.save()

        problem = problems[0]
        context = {
            'problems':problems,
            'exam_ref_id':exam_ref_id,
            'title':title,
            'page':page,
            'problem':problem,
        }
        return render(request,'app_exercise/exam.html',context)
    
    elif request.POST and int(page) > 1 and int(page)!=perround_problem+1:
        try:
            exam_result=result.objects.get(problem_text=str(int(page)-1)+'_nulltext',doing_at =exercise_result.objects.order_by('-id').filter(user_id=user_id).first().doing_at)#+ user_id=user_id
            exam_result.number = int(page)-1
            exam_result.choose = request.POST.get('choose')
            exam_result.correct_c_id = problems[int(page)-2].correct_c_id
            exam_result.problem_text = problems[int(page)-2].problem_text
            if str(request.POST.get('choose')) == str(problems[int(page)-2].correct_c_id):
                exam_result.status = 1

            if str(request.POST.get('choose')) != str(problems[int(page)-2].correct_c_id):
                exam_result.status = 0

            exam_result.doing_at = exercise_result.objects.order_by('-id').filter(user_id=user_id).first().doing_at         #ในอนาคตเพิ่ม .filter(user_id=user_id)
            exam_result.user_id = user_id
            exam_result.save()
        except:
            hello = 'สวัสดี'
        number = int(page)-1
        problem = problems[number]
        context = {
            'problems':problems,
            'exam_ref_id':exam_ref_id,
            'title':title,
            'page':int(page),
            'problem':problem,
        }
        return render(request,'app_exercise/exam.html',context)
    
    elif request.POST and int(page) > 1 and int(page)==perround_problem+1 :
        try:
            exam_result=result.objects.get(problem_text=str(int(page)-1)+'_nulltext',doing_at =exercise_result.objects.order_by('-id').filter(user_id=user_id).first().doing_at)#+ user_id=user_id
            exam_result.number = int(page)-1
            exam_result.choose = request.POST.get('choose')
            exam_result.correct_c_id = problems[int(page)-2].correct_c_id
            exam_result.problem_text = problems[int(page)-2].problem_text
            if str(request.POST.get('choose')) == str(problems[int(page)-2].correct_c_id):
                exam_result.status = 1

            if str(request.POST.get('choose')) != str(problems[int(page)-2].correct_c_id):
                exam_result.status = 0
            exam_result.doing_at = exercise_result.objects.order_by('-id').filter(user_id=user_id).first().doing_at         #ในอนาคตเพิ่ม .filter(user_id=user_id)
            exam_result.user_id = user_id
            exam_result.save()
            latest_result = exercise_result.objects.order_by('-id').first()
            latest_result.total_point = len(result.objects.filter(doing_at=exercise_result.objects.order_by('-id').first().doing_at , status=1))

            latest_result.subject = exercises.objects.get(ref_id=exam_ref_id).title
            latest_result.subject = exercises.objects.get(ref_id=exam_ref_id).subject

            latest_result.save()
        except:
             hello = 'สวัสดี'
        exercise_result.objects.filter(total_point = None).delete()
        context = {
            'problems':problems,
            'exercise':exercises.objects.get(ref_id=exam_ref_id),
            'exercise_results':exercise_result.objects.order_by('-id').filter(user_id=user_id).first(),                 #ในอนาคตเพิ่ม .filter(user_id=user_id)
            'exam_result':result.objects.filter(doing_at=exercise_result.objects.order_by('-id').first().doing_at),
        }

        return render(request,'app_exercise/result.html',context)
    return render(request,'app_exercise/exam.html')
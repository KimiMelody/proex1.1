from django.shortcuts import render ,redirect
from django.http import HttpResponse
from app_general.models import exercises
from .models import exam ,result , exercise_result
#from .forms import ProductForm

# Create your views here.

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
            add_exam.save()
    
    context = {
        'pages':pages,
        'exam_ref_id':exam_ref_id,
        'exercise':exercise,

        'problems':problems,
    }
    return render(request,'app_exercise/detail_exam.html',context)

def pages(request,exam_ref_id,page):
    problems = exam.objects.filter(ref_id=exam_ref_id).order_by('id')
    title = exercises.objects.get(ref_id=exam_ref_id).title
    perround_problem = exercises.objects.get(ref_id=exam_ref_id).perround_problem

    if request.POST and int(page) ==1:
        doing = exercise_result()
        doing.ref_id = exam_ref_id
        doing.max_point = perround_problem
        doing.save()

        exam_result_last = result()
        exam_result_last.problem_text = 'lastexam'
        exam_result_last.doing_at = exercise_result.objects.order_by('-id').first().doing_at         #ในอนาคตเพิ่ม .filter(user_id=user_id)
        exam_result_last.save()

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
        exam_result = result()
        exam_result.number = int(page)-1
        exam_result.choose = request.POST.get('choose')
        exam_result.correct_c_id = problems[int(page)-2].correct_c_id
        exam_result.problem_text = problems[int(page)-2].problem_text
        if str(request.POST.get('choose')) == str(problems[int(page)-2].correct_c_id):
            exam_result.status = 1

        if str(request.POST.get('choose')) != str(problems[int(page)-2].correct_c_id):
            exam_result.status = 0

        exam_result.doing_at = exercise_result.objects.order_by('-id').first().doing_at         #ในอนาคตเพิ่ม .filter(user_id=user_id)
        exam_result.save()

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
            exam_result=result.objects.get(problem_text='lastexam',doing_at =exercise_result.objects.order_by('-id').first().doing_at)#+ user_id=user_id
            exam_result.number = int(page)-1
            exam_result.choose = request.POST.get('choose')
            exam_result.correct_c_id = problems[int(page)-2].correct_c_id
            exam_result.problem_text = problems[int(page)-2].problem_text
            if str(request.POST.get('choose')) == str(problems[int(page)-2].correct_c_id):
                exam_result.status = 1

            if str(request.POST.get('choose')) != str(problems[int(page)-2].correct_c_id):
                exam_result.status = 0
            exam_result.doing_at = exercise_result.objects.order_by('-id').first().doing_at         #ในอนาคตเพิ่ม .filter(user_id=user_id)
            exam_result.save()
            latest_result = exercise_result.objects.order_by('-id').first()
            latest_result.total_point = len(result.objects.filter(doing_at=exercise_result.objects.order_by('-id').first().doing_at , status=1))
            latest_result.save()
        except:
             hello = 'สวัสดี'
        context = {
            'problems':problems,
            'exercise':exercises.objects.get(ref_id=exam_ref_id),
            'exercise_results':exercise_result.objects.order_by('-id').first(),                 #ในอนาคตเพิ่ม .filter(user_id=user_id)
            'exam_result':result.objects.filter(doing_at=exercise_result.objects.order_by('-id').first().doing_at),
        }

        return render(request,'app_exercise/result.html',context)
    return render(request,'app_exercise/exam.html')
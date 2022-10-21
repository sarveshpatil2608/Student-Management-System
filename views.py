from django.shortcuts import render, HttpResponse
from .models import Student, Department, Skills
from datetime import datetime
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_stu(request):
    studs = Student.objects.all()
    context = {
        'studs': studs
    }
    print(context)
    return render(request, 'all_stu.html', context)


def add_stu(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        fees = int(request.POST['fees'])
        paid_fees = int(request.POST['paid_fees'])
        skills = int(request.POST['skills'])
        phone = int(request.POST['phone'])
        # ad_date = request.POST['ad_date']
        new_stu = Student(first_name=first_name, last_name=last_name, dept_id=dept, fees=fees, paid_fees=paid_fees,
                          skills_id=skills, phone=phone, ad_date=datetime.now())
        new_stu.save()
        return HttpResponse("Student added successfully")

    elif request.method == 'GET':
        return render(request, 'add_stu.html')
    else:
        return HttpResponse("Sorry! Some error occurred, Student cannot be added. ")


def remove_stu(request, stu_id=0):
    if stu_id:
        try:
            stu_to_be_removed = Student.objects.get(id=stu_id)
            stu_to_be_removed.delete()
            return HttpResponse("Student removed successfully.")
        except:
            return HttpResponse("Please enter valid student id.")

    studs = Student.objects.all()
    context = {
        'studs': studs
    }
    return render(request, 'remove_stu.html', context)


def filter_stu(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        skills = request.POST['skills']
        studs = Student.objects.all()
        if name:
            studs = studs.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            studs = studs.filter(dept__name__icontains=dept)
        if skills:
            studs = studs.filter(skills__name__icontains=skills)

        context = {
            'studs': studs
        }
        return render(request, 'all_stu.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_stu.html')
    else:
        return HttpResponse("Please enter correct values.")

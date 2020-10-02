from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import *
from users.models import Student
from .decorators import allowed_users
from .forms import *


#meeting operation views for teachers

@login_required(login_url='login_pg')
def dashboard(request):
    user = request.user
    user_grps = user.groups.all()
    group = Group.objects.get(name="Teachers")
    meetings = Meeting.objects.all()

    if group in user_grps:
        meetings = Meeting.objects.filter(subject__teacher=request.user.id, date=date.today(), status="Incomplete")
        context = {'meetings': meetings}
        return render(request, 'main/lst_meetings.html', context)
    else:
        user = request.user
        stu_user = Student.objects.get(user=User.objects.get(username=user))
        stu_std = stu_user.std
        if stu_std == 9:
            stu_meeting = meetings.filter(std=9, status="Incomplete", date=date.today())
        if stu_std == 8:
            stu_meeting = meetings.filter(std=8, status="Incomplete", date=date.today())
        if stu_std == 7:
            stu_meeting = meetings.filter(std=7, status="Incomplete", date=date.today())

        context = {'meetings': stu_meeting}
        return render(request, 'main/student_dash.html', context)

@allowed_users(allowed_roles=['Teachers'])
def list_meetings(request, std):
    meetings = Meeting.objects.filter(std=std, status="Incomplete", date=date.today())
    context = {'meetings': meetings, 'std': std}
    return render(request, 'main/lst_meetings.html', context)

@allowed_users(allowed_roles=['Teachers'])
def today_meets(request, std):
    meetings = Meeting.objects.filter(std=std, date=date.today())
    context = {'meetings': meetings, 'std':std}
    return render(request, 'main/lst_meetings.html', context)

@allowed_users(allowed_roles=['Teachers'])
def all_meets(request, std):
    meetings = Meeting.objects.filter(std=std)
    context = {'meetings': meetings, 'std': std}
    return render(request, 'main/lst_meetings.html', context)

# views for particular teacher to view their meetings
@allowed_users(allowed_roles=['Teachers'])
def my_today_meets(request):
    meetings = Meeting.objects.filter(subject__teacher=request.user.id, date=date.today())
    context = {'meetings': meetings}
    return render(request, 'main/lst_meetings.html', context)

@allowed_users(allowed_roles=['Teachers'])
def my_all_meets(request):
    meetings = Meeting.objects.filter(subject__teacher=request.user.id)
    context = {'meetings': meetings}
    return render(request, 'main/lst_meetings.html', context)

# meeting crud views
@allowed_users(allowed_roles=['Teachers'])
def crt_meeting(request):
    form = MeetingCreationForm()
    if request.method == "POST":
        std = request.POST.get('std')
        form = MeetingCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/meetings-class/{std}')
    context = {'form': form}
    return render(request, 'main/crt_meeting.html', context)

@allowed_users(allowed_roles=['Teachers'])
def edit_meeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    std = request.POST.get('std')
    form = MeetingCreationForm(instance=meeting)
    if request.method == 'POST':
        form = MeetingCreationForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
        return redirect(f'/meetings-class/{std}')
    context = {'form': form, 'edit': True}
    return render(request, 'main/crt_meeting.html', context)

@allowed_users(allowed_roles=['Teachers'])
def del_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    std = meeting.std
    meeting.status = "Deleted"
    meeting.save()
    return redirect(f'/meetings-class/{std}')

@allowed_users(allowed_roles=['Teachers'])
def rest_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    std = meeting.std
    meeting.status = "Incomplete"
    meeting.save()
    return redirect(f'/meetings-class/{std}')

@allowed_users(allowed_roles=['Teachers'])
def con_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    std = meeting.std
    if meeting.status == "Incomplete":
        meeting.status = "Concluded"
        meeting.save()
    else:
        meeting.status = "Incomplete"
        meeting.save()
    return redirect(f'/meetings-class/{std}')

@allowed_users(allowed_roles=['Teachers'])
def meeting_info(request, id):
    meeting = Meeting.objects.get(id=id)
    std = meeting.std
    context = {'meeting': meeting, 'std': std}
    return render(request, 'main/view_student.html', context)

# student management views

@allowed_users(allowed_roles=['Teachers'])
def all_stu(request, std):
    students_a = Student.objects.filter(std=std, div="A")
    students_b = Student.objects.filter(std=std, div="B")
    context = {'students_a': students_a, 'students_b': students_b, 'std': std}
    return render(request, 'main/lst_students.html', context)

@allowed_users(allowed_roles=['Teachers'])
def view_students(request, rollno):
    student = Student.objects.get(rollno=rollno)
    std = student.std
    context = {'student': student, 'std': std}
    return render(request, 'main/view_student.html', context)

@allowed_users(allowed_roles=['Teachers'])
def delte_student(request, rollno):
    student = Student.objects.get(rollno=rollno)
    std = student.std
    stu_user = User.objects.get(username=student.user)
    student.delete()
    stu_user.delete()
    return redirect(f'/students/{std}')
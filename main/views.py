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
        meetings = Meeting.objects.filter(
            subject__teacher=request.user.id, date=date.today(), status="Incomplete").order_by('-id')
        context = {'meetings': meetings}
        return render(request, 'main/lst_meetings.html', context)
    else:
        user = request.user
        stu_user = Student.objects.get(user=User.objects.get(username=user))
        stu_std = stu_user.std
        if stu_std == 9:
            stu_meeting = meetings.filter(std=9, status="Incomplete", date=date.today()).order_by('-id')
        if stu_std == 8:
            stu_meeting = meetings.filter(std=8, status="Incomplete", date=date.today()).order_by('-id')
        if stu_std == 7:
            stu_meeting = meetings.filter(std=7, status="Incomplete", date=date.today()).order_by('-id')

        context = {'meetings': stu_meeting}
        return render(request, 'main/student_dash.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def list_meetings(request, std):
    meetings = Meeting.objects.filter(std=std, status="Incomplete", date=date.today()).order_by('-id')
    context = {'meetings': meetings, 'std': std}
    return render(request, 'main/lst_meetings.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def today_meets(request, std):
    meetings = Meeting.objects.filter(std=std, date=date.today()).order_by('-id')
    context = {'meetings': meetings, 'std':std}
    return render(request, 'main/lst_meetings.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def all_meets(request, std):
    meetings = Meeting.objects.filter(std=std).order_by('-id')
    context = {'meetings': meetings, 'std': std}
    return render(request, 'main/lst_meetings.html', context)

# views for particular teacher to view their meetings
@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def my_today_meets(request):
    meetings = Meeting.objects.filter(subject__teacher=request.user.id, date=date.today()).order_by('-id')
    context = {'meetings': meetings}
    return render(request, 'main/lst_meetings.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def my_all_meets(request):
    meetings = Meeting.objects.filter(subject__teacher=request.user.id).order_by('-id')
    context = {'meetings': meetings}
    return render(request, 'main/lst_meetings.html', context)

# meeting crud views
@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def crt_meeting(request):
    form = MeetingCreationForm()
    if request.method == "POST":
        std = request.POST.get('std')
        form = MeetingCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/meetings-class/{std}/')
    context = {'form': form}
    return render(request, 'main/crt_meeting.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def edit_meeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    std = request.POST.get('std')
    form = MeetingCreationForm(instance=meeting)
    if request.method == 'POST':
        form = MeetingCreationForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
        return redirect(f'/meetings-class/{std}/')
    context = {'form': form, 'edit': True}
    return render(request, 'main/crt_meeting.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def del_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    std = meeting.std
    meeting.status = "Deleted"
    meeting.save()
    return redirect(f'/meetings-class/{std}/')

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def rest_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    std = meeting.std
    meeting.status = "Incomplete"
    meeting.save()
    return redirect(f'/meetings-class/{std}/')

@login_required(login_url='login_pg')
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
    return redirect(f'/meetings-class/{std}/')

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def meeting_info(request, id):
    meeting = Meeting.objects.get(id=id)
    participents = meeting.participents.all()
    participents_count = meeting.participents.count()
    participents_a = participents.filter(div="A")
    participents_b = participents.filter(div="B")
    std = meeting.std
    total_students = Student.objects.filter(std=std).count()
    try:
        o_attendance = participents_count/total_students*100
    except:
        o_attendance = 0
    context = {'meeting': meeting, 'std': std, 'participents_a': participents_a, 'participents_b': participents_b,
               'participents_count': participents_count, 'total_students': total_students, 'o_attendance': o_attendance}
    return render(request, 'main/view_student.html', context)

# student management views

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def all_stu(request, std):
    students_a = Student.objects.filter(std=std, div="A").order_by('rollno')
    students_b = Student.objects.filter(std=std, div="B").order_by('rollno')
    context = {'students_a': students_a, 'students_b': students_b, 'std': std}
    return render(request, 'main/lst_students.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def view_students(request, rollno):
    student = Student.objects.get(rollno=rollno)
    std = student.std
    # meeting_p = Meeting.participents.all()
    meeting_a = Meeting.objects.filter(participents=student)
    meetings_count = meeting_a.count()
    a_meet_c = Meeting.objects.filter(std=std).count()
    try:
        over_all_attendance = meetings_count/a_meet_c*100
    except:
        over_all_attendance = 0
    context = {'student': student, 'std': std, 'meetings_attended': meeting_a, 'meeting_count': meetings_count,
               'a_meet_c': a_meet_c, 'over_all_attendance': over_all_attendance}
    return render(request, 'main/view_student.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Teachers'])
def delte_student(request, rollno):
    student = Student.objects.get(rollno=rollno)
    std = student.std
    stu_user = User.objects.get(username=student.user)
    student.delete()
    stu_user.delete()
    return redirect(f'/students/{std}/')


 # student dash operation views

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Students'])
def student_today_meets(request):
    student = Student.objects.get(user=request.user)
    std = student.std
    meetings = Meeting.objects.filter(std=std, date=date.today()).order_by('-id')
    context = {'meetings': meetings}
    return render(request, 'main/student_dash.html', context)

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Students'])
def student_all_meets(request):
    student = Student.objects.get(user=request.user)
    std = student.std
    meetings = Meeting.objects.filter(std=std).order_by('-id')
    context = {'meetings': meetings}
    return render(request, 'main/student_dash.html', context)

#  marking attendance views

@login_required(login_url='login_pg')
@allowed_users(allowed_roles=['Students'])
def mark_attendance(request, id):
    meeting = Meeting.objects.get(id=id)
    student = Student.objects.get(user=request.user)
    participents = [meeting.participents]
    meeting.participents.add(student)
    meeting.save()
    return redirect("dashboard_pg")




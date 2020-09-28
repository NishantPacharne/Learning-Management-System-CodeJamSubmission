from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentCreationForm, TeacherCreatinForm
from .models import Student, Teacher
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_pg')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_pg')
            else:
                messages.info(request, 'Invalid credentials given , please try again !')
                return render(request, 'users/login.html')
        return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login_pg')

def student_register(request):
    if request.user.is_authenticated:
        return redirect('dashboard_pg')
    else:
        form = StudentCreationForm()
        if request.method == "POST":
            form = StudentCreationForm(request.POST)
            if form.is_valid():
                user = request.POST['username']
                fathers_name = request.POST['fathers_name']
                std = request.POST['std']
                div = request.POST['div']
                rollno = request.POST['rollno']
                password = request.POST['password1']
                if Student.objects.filter(std=std, div=div, rollno=rollno).exists():
                    messages.info(request, 'A Student in your class with that roll no already exists')
                    return render(request, 'users/register.html', {'form': form})
                else:
                    usr = form.save()
                    Student(user=User.objects.filter(username=user).first(), father_name=fathers_name, std=std, div=div, rollno=rollno).save()
                    group = Group.objects.get(name='Students')
                    usr.groups.add(group)
                    usr = authenticate(username=user, password=password)
                    login(request, usr)
                    return redirect('dashboard_pg')

        context = {'form': form}
        return render(request, 'users/register.html', context)

def teacher_register(request):
    if request.user.is_authenticated:
        return redirect('home_pg')
    else:
        form = TeacherCreatinForm()
        if request.method == "POST":
            form = TeacherCreatinForm(request.POST)
            if request.POST['vrf_cd'] == "N0716":
                if form.is_valid():
                    user = request.POST['username']
                    password = request.POST['password1']
                    usr = form.save()
                    Teacher(user=User.objects.filter(username=user).first()).save()
                    group = Group.objects.get(name='Teachers')
                    usr.groups.add(group)
                    usr = authenticate(username=user, password=password)
                    login(request, usr)
                    return redirect('dashboard_pg')
            else:
                form = TeacherCreatinForm(request.POST)
                messages.info(request, 'Wrong verification code, please try again!')
                return render(request, 'users/t_register.html', {'form': form})

        context = {'form': form}
        return render(request, 'users/t_register.html', context)

def reset_password(request):
    return HttpResponse("It is Working")


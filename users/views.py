from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentCreationForm, TeacherCreatinForm
from .models import Student, Teacher, UserOtp
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_pg')
    else:
        if request.method == "POST":
            recieved_otp = request.POST.get('otp')
            if recieved_otp:
                otp_usr = request.POST.get('usr')
                usr = User.objects.get(username=otp_usr)
                if int(recieved_otp) == UserOtp.objects.filter(user=usr).last().otp:
                    usr.is_active = True
                    usr.save()
                    login(request, usr)
                    return redirect('dashboard_pg')
                else:
                    return render(request, 'users/otp.html', {'title': 'Enter OTP', 'text':'You have entered a wrong OTP', 'usr': usr})
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_pg')
            elif not User.objects.filter(username=username).exists():
                messages.info(request, 'Invalid credentials given , please try again !')
                return render(request, 'users/login.html')
            elif not User.objects.get(username=username).is_active:
                usr = User.objects.get(username=username)
                context = {'title': "Enter Your OTP", 'usr': usr}
                return render(request, 'users/otp.html', context)
            else:
                messages.info(request, 'Invalid credentials given , please try again !')
                return render(request, 'users/login.html')
        return render(request, 'users/login_demo_pg.html')

def student_demo_login(request):
    username = 'jsd16'
    password = 'hackathon'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard_pg')

def teacher_demo_login(request):
    username = 'nmp16'
    password = 'hackathon'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard_pg')


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
                    Student(user=User.objects.filter(username=user).first(), father_name=fathers_name, std=std, div=div,
                            rollno=rollno).save()
                    group = Group.objects.get(name='Students')
                    usr.groups.add(group)
                    usr.is_active = False
                    usr.save()
                    # otp management
                    if UserOtp.objects.filter(user=usr).exists():
                        return render(request, 'users/error_messages.html',
                                      {'title': 'A OTP is already sent , pls check your mailbox'})
                    else:
                        usr_otp = random.randint(100000, 999999)
                        UserOtp.objects.create(user=usr, otp=usr_otp).save()
                        e_meesage = f"Hi {usr.first_name} This is Nishant From NCONNECT, \n Your OTP is {usr_otp}\n Thank You Have a Nice Day ahead !"
                        send_mail(
                            "Welcome To N-CONNECT , Verification Email",
                            e_meesage,
                            settings.EMAIL_HOST_USER,
                            [usr.email],
                            fail_silently=False
                        )
                        messages.success(request, f'Account for {user} has been created succesfully !')
                        return redirect('login_pg')
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
                    usr.is_active = False
                    usr.save()
                    # otp management
                    usr_otp = random.randint(100000, 999999)
                    UserOtp.objects.create(user=usr, otp=usr_otp)
                    e_meesage = f"Hi {usr.first_name} This is Nishant From NCONNECT, \n Your OTP is {usr_otp}\n Thank You Have a Nice Day ahead !"
                    send_mail(
                        "Welcome To N-CONNECT , Verification Email",
                        e_meesage,
                        settings.EMAIL_HOST_USER,
                        [usr.email],
                        fail_silently=False
                    )
                    messages.success(request, f'Account for {usr.first_name} {usr.last_name} has been created succesfully !')
                    return redirect('login_pg')
            else:
                form = TeacherCreatinForm(request.POST)
                messages.info(request, 'Wrong verification code, please try again!')
                return render(request, 'users/t_register.html', {'form': form})

        context = {'form': form}
        return render(request, 'users/t_register.html', context)


from asyncio import Handle

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
from studentapp.models import Details


def homePage(request):
    return render(request,'home.html')

def formPage(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        mail = request.POST.get('mail')
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')

        details_instance = Details.objects.create(name=name, phone=phone, dob=dob, mail=mail, gender=gender, department=department, course=course, purpose=purpose )
        # return HttpResponse("Details submitted successfully!")
        return redirect('homepage')
    else:
        return render(request, 'detailform.html')

    return render(request,'detailform.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm-password')

        if pass1!=pass2:
            return HttpResponse("Passswords dos not match")
        else:
            # print(uname,email,pass1,pass2)
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return HttpResponse("User has been created sucessfully...")
            return redirect('login')
    return render(request,'signup.html')

def loginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        print(uname,pass1)
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('detailform')
        else:
            return HttpResponse("Username or Password incorrect..")

    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return render(request,'login.html')
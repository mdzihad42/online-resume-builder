from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from protfolio.models import*
from protfolio.forms import*

def registerPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_exists=userModel.objects.filter(username=username).exists()
        if user_exists:
            messages.warning(request,'user already exists')
        if password==confirm_password:
            userModel.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('loginPage')
    return render(request,'auth/register.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('homePage')
    return render(request,'auth/login.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')
@login_required
def homePage(request):
    profile = profileModel.objects.filter(created_by=request.user).last()
    project=projectModel.objects.filter(created_by=request.user)
    work2=workExModel.objects.filter(created_by=request.user).last()
    work=workExModel.objects.filter(created_by=request.user)
    edu=EduModel.objects.filter(created_by=request.user)
    return render (request,'base.html',{'profile':profile,
                                        'email_data':request.user,
                                        'work':work,
                                        'edu':edu,
                                        'project':project,
                                        'work2':work2
                                        })
@login_required
def addDetails(request):
    if request.method=='POST':
        project=projectForm(request.POST)
        work=workForm(request.POST)
        edu=eduForm(request.POST)
        if project.is_valid():
            form=project.save(commit=False)
            form.created_by=request.user
            form.save()
            return redirect('addDetails')
        if work.is_valid():
            form=work.save(commit=False)
            form.created_by=request.user
            form.save()
            return redirect('addDetails')
        if edu.is_valid():
            form=edu.save(commit=False)
            form.created_by=request.user
            form.save()
            return redirect('addDetails')
    else:
        project=projectForm()
        work=workForm()
        edu=eduForm()
        
    return render (request,'project/projectAdd.html',{
                                        'work':work,
                                        'edu':edu,
                                        'project':project
                                        })
@login_required
def profilePage(request):
    current_user = request.user
    profile_data, created = profileModel.objects.get_or_create(created_by=current_user)

    if request.method=='POST':
        profile_pic=request.FILES.get('profile_pic')
        profile_data.full_name = request.POST.get('full_name')
        profile_data.phone = request.POST.get('phone')
        profile_data.address = request.POST.get('address')

        if profile_pic:
            profile_data.profile_pic = profile_pic

        profile_data.save()
        return redirect('update')

    return render(request,'profile/profile.html', {'profile': profile_data})

@login_required
def update(request):
    
    return render (request,'profile/update.html')
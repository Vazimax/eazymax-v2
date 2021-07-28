from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login
from django.shortcuts import render , redirect  
from django.contrib import messages 
from post.models import Post
from project import settings
from .models import Profile
from .forms import *

def policy(request):

    return render(request,'policy/policy.html')


def register(request):
    if request.user.is_authenticated :
 	    return redirect('home')
    else :
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                messages.success(request,'Votre compte à été créé avec succès / لقد تم انشاء حسابك بنجاح ')
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect(f'/profile/{user.profile.id}{-1}/edit')
        else : 
            form = UserRegisterForm()

        context = {
            'form':form,
            'title' : 'Register'
        }

        return render(request,'register.html',context)

# def loginPage(request):
#     if request.user.is_authenticated :
# 		    return redirect('home')

#     else :  
#         if request.method == 'POST':
#                 email = request.POST.get('email')
#                 password = request.POST.get('password')    

#                 user = authenticate(request,email=email,password=password)

#                 if user is not None:
#                         login(request, user)
#                         return redirect('home')
#                 else:
#                     messages.info(request, 'Username OR password is incorrect')

#         context = {

#         }
#         return render(request,'login.html',context)

@login_required
def profile(request,id):
    profile = Profile.objects.get(user=id)

    posts = Post.objects.filter(poster_id=id)


    context = {
        'profile' : profile, 
        'posts' : posts,
    }

    return render(request,'profile.html',context)

@login_required
def profile_edit(request,id):
    profile = Profile.objects.get(user=id)

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        u_form = UserForm(request.POST,instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            my_profile = p_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(f'/profile/{profile.id}/edit')

    else :
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request,'profile_edit.html',context)
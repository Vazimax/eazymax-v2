from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView , DeleteView
from django.http.response import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime as dt
from django.urls import reverse
from user.models import Profile
from datetime import timedelta
from .forms import PostForm
from .models import Post
from .filters import *
from pytz import *
import random 
import pytz


def home(request):
    featured_posts = list(Post.objects.filter(featured = True))
    featured_jobs = random.sample(featured_posts,3)


    posts = Post.objects.all()

    profiles = Profile.objects.all()

    filter = JobFilter(request.GET,queryset=posts)
    posts = filter.qs

    context = {
        'featured_posts' : featured_jobs,
        'posts' : posts,
        'filter' : filter,
        'profiles' : profiles,
    }
    return render(request,'home.html',context)

def about_us(request):

    return render(request,'about_us.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        comments = request.POST['comments']

        send_mail(
            subject,
            comments,
            email,
            ['tvazimax@gmail.com'],
        )

        context = {
            'email' : email,
            'subject' : subject,
            'comments' : comments,
        }
        return render(request,'contact.html',context)

    else :
        return render(request,'contact.html')

def membership(request):

    return render(request,'membership.html')

def order_done(request):

    return render(request,'order_done.html')

def jobs(request):
    posts = Post.objects.all()

    filter = JobFilter(request.GET,queryset=posts)
    posts = filter.qs

    paginator = Paginator(posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : page_obj,
        'filter' : filter,
    }
    return render(request,'jobs.html',context)

@login_required
def post_job(request):

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        yesterday = dt.now() - timedelta(days=1)
        if Post.objects.filter(poster=request.user, date_posted__gt=yesterday).exists():
            return HttpResponseForbidden("Vous avez posté aujourd'hui, venez demain ! / ! لقد نشرت اليوم ، تعال غدًا")
        elif form.is_valid():
            my_form = form.save(commit=False)
            my_form.poster = request.user
            my_form.save()
            messages.success(request,"Vous avez créé un post avec succès / قمت بإنشاء منشور بنجاح")
            return redirect(f'/post/{my_form.id}')
        else :
            messages.error(request,"le numéro de téléphone n'est pas correct / رقم الهاتف غير صحيح")
    else :
        form = PostForm()


    context = {
        'form' : PostForm(),
    }
    return render(request,'post_job.html',context)

def post_detail(request,pk):

    object = Post.objects.get(id=pk)

    posts = list(Post.objects.filter(featured = False))
    posts = random.sample(posts,2)
    
    featured_posts = list(Post.objects.filter(featured = True))
    featured_posts = random.sample(featured_posts,2)

    context = {
        'object' : object,
        'posts' : posts,
        'featured_posts' : featured_posts,
    }

    return render(request,'post_detail.html',context)


@login_required
def UpdatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Votre post a été mis à jour avec succès / تم تحديث منشورك بنجاح')
            return redirect(f'/post/{post.id}')
        else :
            messages.error(request,"le numéro de téléphone n'est pas correct / رقم الهاتف غير صحيح")
            
    context = {
        'form':form
    }

    return render(request,'post_edit.html',context)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        else :
            return False

def plumber(request):
    jobs = Post.objects.filter(category=5)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/plumber.html',context)

def electrician(request):
    jobs = Post.objects.filter(category=4)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/plumber.html',context)

def dishwasher(request):
    jobs = Post.objects.filter(category=2)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/dishwasher.html',context)


def carpenter(request):
    jobs = Post.objects.filter(category=1)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : page_obj,
        'filter' : filter,
    }
    return render(request,'categories/carpenter.html',context)

def painter(request):
    jobs = Post.objects.filter(category=3)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : page_obj,
        'filter' : filter,
    }
    return render(request,'categories/painter.html',context)


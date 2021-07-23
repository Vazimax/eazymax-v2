from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView , DeleteView
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from user.models import Profile
from .forms import PostForm
from .models import Post
from .filters import *
import random


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
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.poster = request.user
            my_form.save()
            messages.success(request,'You created a post successefully')
            return redirect(f'/post/{my_form.id}')
    else :
        form = PostForm()

    context = {
        'form' : PostForm(),
    }
    return render(request,'post_job.html',context)

def post_detail(request,pk):

    object = Post.objects.get(id=pk)
    posts = list(Post.objects.all())
    featured_posts = random.sample(posts,3)

    context = {
        'object' : object,
        'featured_posts' : featured_posts,
    }

    return render(request,'post_detail.html',context)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','image','description','category','phone_number']

    def form_valid(self,form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        else :
            return False

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



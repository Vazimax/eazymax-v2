from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime as dt
from django.urls import reverse
from datetime import timedelta

from .forms import PostForm , ReviewForm
from .models import Post , Review
from user.models import Profile
from .filters import *
from pytz import *
import random
import pytz

from django.core.mail import send_mail
from django.http import JsonResponse
from django.db.models import Q
import datetime
import json

def home(request):
        
        if request.user.is_authenticated :
            user = Profile.objects.get(user_id=request.user.id)
        else : 
            user = None

        try:
            if  user.expiredate < datetime.datetime.now():
                usr=Profile.objects.filter(user_id=request.user.id)
                usr.update(sta=False,prem=False,vip=False,maxed=False,expiredate=None)
        except:
                pass
        
        if Post.objects.filter(hot = True).count() >= 5 :
            featured_posts = list(Post.objects.filter(hot = True))
            featured_jobs = random.sample(featured_posts,5)
        elif Post.objects.filter(hot = True).count() >= 4 :
            featured_posts = list(Post.objects.filter(hot = True))
            featured_jobs = random.sample(featured_posts,4)
        elif Post.objects.filter(hot = True).count() >= 3 :
            featured_posts = list(Post.objects.filter(hot = True))
            featured_jobs = random.sample(featured_posts,3)
        elif Post.objects.filter(hot = True).count() >= 2 :
            featured_posts = list(Post.objects.filter(hot = True))
            featured_jobs = random.sample(featured_posts,2)
        elif Post.objects.filter(hot = True).count() >= 1 :
            featured_posts = list(Post.objects.filter(hot = True))
            featured_jobs = random.sample(featured_posts,1)
        else :
            featured_jobs = ''    
            
        posts = Post.objects.filter(poster_id=request.user.id)
        if Profile.objects.filter(Q(vip=True) | Q(sta=True) | Q(prem=True)).count() >= 6 :
            profilex = list(Profile.objects.filter(Q(vip=True) | Q(sta=True) | Q(prem=True)))
            profiles = random.sample(profilex,6)
        elif Profile.objects.filter(Q(vip=True) | Q(sta=True) | Q(prem=True)).count() >= 3 : 
            profilex = list(Profile.objects.filter(Q(vip=True) | Q(sta=True) | Q(prem=True)))
            profiles = random.sample(profilex,3)
        elif Profile.objects.filter(Q(vip=True) | Q(sta=True) | Q(prem=True)).count() >= 1 : 
            profilex = list(Profile.objects.filter(Q(vip=True) | Q(sta=True) | Q(prem=True)))
            profiles = random.sample(profilex,1)
        else : 
            profiles = ''

        filter = JobFilter(request.GET, queryset=posts)
        posts = filter.qs

        if request.user.is_authenticated :
            if user.sta or user.prem or user.vip:
                posts = Post.objects.all()
                for post in posts :
                    if post.poster.profile.id == user.id :
                        post.hot = True    
            else:
                pass

        userx = user
        
        context = {
            'featured_posts': featured_jobs,
            'posts': posts,
            'filter': filter,
            'profiles': profiles,
            'userx': userx,
            }

        return render(request, 'home.html', context)

def memberships(request):
    if request.user.is_authenticated :
        user = Profile.objects.get(user_id=request.user.id)
    else : 
        user = None
    
    return render(request,'memberships.html',{'userx':user,'title':'memberships'})

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        comments = request.POST['comments']

        send_mail(
            subject,
            comments,
            email,
            ['eazymax.v2@gmail.com'],
        )

        context = {
            'email' : email,
            'subject' : subject,
            'comments' : comments,
            'title':'contact'
        }
        return render(request,'contact.html',context)

    else :
        return render(request,'contact.html')


def about_us(request):

    return render(request, 'about_us.html',{'title':'à propos de nous - معلومات عنا'})


def membershipsta(request):
    if request.user.is_authenticated:
        return render(request, 'membershipsta.html',{'title':'membership 1'})
    else:
        return redirect('login')


def membershipprem(request):
    if request.user.is_authenticated:
        return render(request, 'membershipprem.html',{'title':'membership 2'})
    else:
        return redirect('login')


def membershipvip(request):
    if request.user.is_authenticated:
        return render(request, 'membershipvip.html',{'title':'membership 3'})
    else:
        return redirect('login')



def order_done(request):
    if request.method == "POST":
        usr = Profile.objects.filter(user_id=request.user.id)
        body = json.loads(request.body)
        tday=datetime.datetime.now()
        ex1=tday + datetime.timedelta(days=2)
        ex2=tday + datetime.timedelta(days=7)
        ex3=tday + datetime.timedelta(days=10)
        if '1.67' in str(body.values()):
            usr.update(sta=True,expiredate=ex1.strftime("%Y-%m-%d"))
        if '3.35' in str(body.values()):
                       usr.update(sta=True,expiredate=ex2.strftime("%Y-%m-%d"))

        if '5.58' in str(body.values()):
                        usr.update(sta=True,expiredate=ex3.strftime("%Y-%m-%d"))

        print(usr.sta.date)
    return render(request, 'order_done.html',{'title':'la demande est faite - تم الطلب'})


def jobs(request):
    posts = Post.objects.all()

    filter = JobFilter(request.GET, queryset=posts)
    posts = filter.qs

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'filter': filter,
        'title' : 'travaux - وظائف'
    }
    return render(request, 'jobs.html', context)


@login_required
def post_job(request):
    user = Profile.objects.get(user_id=request.user.id)
    post = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        yesterday = dt.now() - timedelta(days=1)
        if Post.objects.filter(poster=request.user, date_posted__gt=yesterday).exists():
            return HttpResponseForbidden("Vous avez posté aujourd'hui, venez demain ! / ! لقد نشرت اليوم ، تعال غدًا")
        elif form.is_valid():
            my_form = form.save(commit=False)
            my_form.poster = request.user
            if user.sta  or user.prem or user.vip:
                my_form.hot = True
            else:
                my_form.hot = False

            user.save()
            my_form.save()
            messages.success(
                request, "Vous avez créé un post avec succès / قمت بإنشاء منشور بنجاح")
            return redirect(f'/post/{my_form.id}')
        else:
            return HttpResponseForbidden("le numéro de téléphone n'est pas correct / رقم الهاتف غير صحيح")
    else:
        form = PostForm()

    context = {
        'form': PostForm(),
        'title' : 'publier une travail - انشر وظيفة'
    }
    return render(request, 'post_job.html', context)


def post_detail(request, pk):

    object = Post.objects.get(id=pk)
    posts = list(Post.objects.filter(hot=False))
    posts = random.sample(posts, 2)

    featured_posts = list(Post.objects.filter(hot=True))
    featured_posts = random.sample(featured_posts, 2)

    reviews = Review.objects.filter(post=object)


    context = {
        'object': object,
        'posts': posts,
        'featured_posts': featured_posts,
        'title' : 'détail de la publication - تفاصيل المنشور',
        'reviews' : reviews
    }

    return render(request, 'post_detail.html', context)


@login_required
def UpdatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Votre post a été mis à jour avec succès / تم تحديث منشورك بنجاح')
            return redirect(f'/post/{post.id}')
        else:
            messages.error(
                request, "le numéro de téléphone n'est pas correct / رقم الهاتف غير صحيح")

    context = {
        'form': form,
        'title' : 'poster la mise à jour - تحديث منشور'
    }

    return render(request, 'post_edit.html', context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        else:
            return False


def plumber(request):
    jobs = Post.objects.filter(category=5)

    filter = JobFilter2(request.GET, queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'filter': filter,
        'title' : 'plombier - اصلاح الماء'
    }
    return render(request, 'categories/plumber.html', context)


def electrician(request):
    jobs = Post.objects.filter(category=4)

    filter = JobFilter2(request.GET, queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'filter': filter,
        'title' : 'électricien - اصلاح الكهرباء'
    }
    return render(request, 'categories/electrician.html', context)


def dishwasher(request):
    jobs = Post.objects.filter(category=2)

    filter = JobFilter2(request.GET, queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'filter': filter,
        'title' : ' Entretien ménager - التدبير المنزلي'
    }
    return render(request, 'categories/dishwasher.html', context)


def carpenter(request):
    jobs = Post.objects.filter(category=1)

    filter = JobFilter2(request.GET, queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'title' : 'charpenterie - نجارة',
        'filter': filter,
    }
    return render(request, 'categories/carpenter.html', context)


def painter(request):
    jobs = Post.objects.filter(category=3)

    filter = JobFilter2(request.GET, queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'title' : 'peintre - صباغ',
        'filter': filter,
    }
    return render(request, 'categories/painter.html', context)

@login_required
def Reviews(request,pk):
    post = Post.objects.get(id=pk)  
    user = request.user

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.post = post
            rate.save()
            return HttpResponseRedirect(reverse('post-detail',args=[pk]))
    else :
        form = ReviewForm()

    context = {
        'form' : form,
        'post' : post,
        'title' : 'Review'
    }
    return render(request,'review.html',context)
from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.db.models import Sum
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UpdateProfileForm, NewHoodForm,NewPostForm,NewBusinessForm
from .models import Profile,Neighbourhood,Business,Post


def home(request,id):
    current_user = request.user
    hood = Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(hood_id=id)
    businesses = Business.objects.filter(biz_hood=id)
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner=current_user
            post.profile=profile
            post.hood = hood
            post.save()
            return redirect(home,id)
    else:
        form = NewPostForm()
    return render(request,'home.html',{'hood':hood,'form':form,'posts':posts,'businesses':businesses})

@login_required(login_url='/accounts/login/')
def setup_hood(request):
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
            return redirect('setup_profile_hood')
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.headman=current_user
            hood.save()
            return redirect(home,hood.id)
    else:
        form = NewHoodForm()
    return render(request,'create_hood/new_hood.html',{'form':form,'user':current_user})



@login_required(login_url='/accounts/login/')
def setup_profile(request,id):
    try:
        profile = Profile.objects.get(user=request.user)
        return redirect(home,id)
    except ObjectDoesNotExist:   
        current_user = request.user
        hood = Neighbourhood.objects.get(id=id)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user_id=request.user.id
                profile.neighbourhood=hood
                profile.save()
                hood.members_count+1
                return redirect(home,id)
        else:
            form = UpdateProfileForm()
    return render(request,'choose_hood/setup_hood_profile.html',{'form':form,'user':current_user,'hood':hood})

@login_required(login_url='/accounts/login/')
def setup_profile_hood(request):
    current_user = request.user
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=request.user.id
            profile.save()
            return redirect(setup_hood)
    else:
        form = UpdateProfileForm()
    return render(request,'setup_profile.html',{'form':form,'user':current_user,})


@login_required(login_url='/accounts/login/')
def choose_hood(request):
    try:
        profile = Profile.objects.get(user_id=request.user.id)
        hood = Neighbourhood.objects.get(headman = request.user.id)
        return redirect(home,hood.id)
    except ObjectDoesNotExist:
            
        hoods = Neighbourhood.objects.all()
        current_user = request.user
    return render(request,'choose_hood.html',{'hoods':hoods,'user':current_user})


@login_required(login_url='/accounts/login/')
def user_profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id) 
    profile = Profile.objects.get(user_id=id)  
    posts = Post.objects.filter(owner=id)       
    return render(request,'profile/profile.html',{'user':user,'profile':profile,'current_user':current_user,'posts':posts})


# view function for the updating profile  page
@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=id
            profile.save()
            return redirect(profile1,id)
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':user,'form':form})

@login_required(login_url='/accounts/login/')
def business(request,id):
    businesses = Business.objects.filter(biz_hood=id)
    current_hood = Neighbourhood.objects.get(id=id) 
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.biz_user=current_user
            biz.biz_hood = current_hood
            biz.save()
            return redirect(business,id)
    else:
        form = NewBusinessForm()
    return render(request,'business.html',{'user':current_user,'form':form,'hood':current_hood,'businesses':businesses})


def  leave_hood(request):
    user = Profile.objects.get(user=request.user)
    user.delete()
    try:
        admin_hood = Neighbourhood.objects.get(headman=request.user)
        admin_hood.delete()
        return redirect(choose_hood)
    except ObjectDoesNotExist:
        return redirect(choose_hood)

    
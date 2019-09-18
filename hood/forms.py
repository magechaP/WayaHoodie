from django import forms
from .models import Profile,Post,Neighbourhood,Business
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighbourhood']


class NewHoodForm(forms.ModelForm):
    class Meta:
        model =Neighbourhood
        exclude = ['headman','members_count']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner','post_date','hood','profile']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['biz_user','biz_hood']
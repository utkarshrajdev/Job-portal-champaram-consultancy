from django import forms
from .models import Profile, Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'country', 'location',
                  'resume', 'grad_year', 'looking_for']


class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
        

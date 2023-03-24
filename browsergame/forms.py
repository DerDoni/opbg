from django import forms
from .models import Skill
from django.contrib.auth.forms import AuthenticationForm

class SkillForm(forms.Form):
    skill = forms.ModelChoiceField(queryset=Skill.objects.all())


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

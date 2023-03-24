from django import forms
from .models import Skill

class SkillForm(forms.Form):
    skill = forms.ModelChoiceField(queryset=Skill.objects.all())

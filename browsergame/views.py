from django.shortcuts import render, redirect
from .models import PvPMatch, Player, Skill
from .forms import SkillForm
from django.http import HttpRequest
import random



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    context = {
        'title': 'Home Page',
        'content': 'Welcome to my game!'
    }
    return render(request, 'home.html', context)
from django.http import HttpResponse

def test_view(request):
    return HttpResponse('Hello, world!')

#def pvp_match(request):
#    match = PvPMatch.objects.last()
#    if match is not None:
#        player1 = match.player1
#        player2 = match.player2
#        npc = match.npc
#        skill_form = SkillForm()
#        context = {
#            'player1': player1,
#            'player2': player2,
#            'npc': npc,
#            'skill_form': skill_form,
#        }
#        if request.method == 'POST':
#            skill_form = SkillForm(request.POST)
#            if skill_form.is_valid():
#                skill = skill_form.cleaned_data['skill']
#                match.turn += 1
#                if match.turn % 2 == 1:
#                    player1_skill = skill
#                    player2_skill = None
#                else:
#                    player2_skill = skill
#                    player1_skill = None
#                player1_damage, player2_damage = calculate_damage(player1, player2, npc, player1_skill, player2_skill)
#                player1.health -= player2_damage
#                player2.health -= player1_damage
#                if player1.health <= 0:
#                    match.winner = player2
#                elif player2.health <= 0:
#                    match.winner = player1
#                match.save()
#                return redirect('pvp_match')
#        return render(request, 'pvp_match.html', context)
#    else:
#        return redirect('create_pvp_match')

def calculate_damage(player1, player2, npc, player1_skill, player2_skill):
    player1_damage = player1.ad
    player2_damage = player2.ad
    if player1_skill is not None:
        if player1_skill.type == Skill.ATTACK:
            player1_damage += player1_skill.damage_modifier
            if player1_skill.critical_chance > random.random():
                player1_damage *= 2
        elif player1_skill.type == Skill.HEAL:
            player1.health += player1_skill.damage_modifier
            if player1.health > 100:
                player1.health = 100
    if player2_skill is not None:
        if player2_skill.type == Skill.ATTACK:
            player2_damage += player2_skill.damage_modifier
            if player2_skill.critical_chance > random.random():
                player2_damage *= 2
        elif player2_skill.type == Skill.HEAL:
            player2.health += player2_skill.damage_modifier
            if player2.health > 100:
                player2.health = 100
    return player1_damage, player2_damage

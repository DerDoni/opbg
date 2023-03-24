from django.db import models
from enumfields import EnumField


class Player(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField()
    ad = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    reflex = models.IntegerField()

    def __str__(self):
        return self.name

class NPC(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField()
    ad = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    reflex = models.IntegerField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    TRANSFORMATION = 'transformation'
    DEBUFF = 'debuff'
    BUFF = 'buff'
    CURSE = 'curse'
    ATTACK = 'attack'
    HEAL = 'heal'
    SKILL_TYPE_CHOICES = [
        (TRANSFORMATION, 'Transformation'),
        (DEBUFF, 'Debuff'),
        (BUFF, 'Buff'),
        (CURSE, 'Curse'),
        (ATTACK, 'Attack'),
        (HEAL, 'Heal'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=SKILL_TYPE_CHOICES)
    accuracy = models.FloatField()
    damage_modifier = models.FloatField()
    critical_chance = models.FloatField()

    def __str__(self):
        return self.name

class PvPMatch(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player2')
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, related_name='matches')
    turn = models.IntegerField(default=0)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='victories', null=True, blank=True)

    def __str__(self):
        return f'{self.player1} vs. {self.player2}'

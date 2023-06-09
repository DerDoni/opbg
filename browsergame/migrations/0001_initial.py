# Generated by Django 4.1.7 on 2023-03-24 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('health', models.IntegerField()),
                ('ad', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('reflex', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('health', models.IntegerField()),
                ('ad', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('reflex', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('transformation', 'Transformation'), ('debuff', 'Debuff'), ('buff', 'Buff'), ('curse', 'Curse'), ('attack', 'Attack'), ('heal', 'Heal')], max_length=255)),
                ('accuracy', models.FloatField()),
                ('damage_modifier', models.FloatField()),
                ('critical_chance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PvPMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.IntegerField(default=0)),
                ('npc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='browsergame.npc')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player1', to='browsergame.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_player2', to='browsergame.player')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='victories', to='browsergame.player')),
            ],
        ),
    ]

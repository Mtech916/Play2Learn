# Generated by Django 4.2.5 on 2023-11-04 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_gamereview_one_review_per_player_per_game'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='gamereview',
            name='One_review_per_player_per_game',
        ),
    ]
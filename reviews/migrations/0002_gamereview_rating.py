# Generated by Django 4.2.5 on 2023-10-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamereview',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')], default=5),
            preserve_default=False,
        ),
    ]
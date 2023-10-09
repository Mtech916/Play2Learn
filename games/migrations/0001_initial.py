# Generated by Django 4.2.5 on 2023-10-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField()),
                ('game', models.TextField(choices=[('MATH', 'Math Facts Practice'), ('ANAGRAM', 'Anagram Hunt')], default='MATH')),
                ('score', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
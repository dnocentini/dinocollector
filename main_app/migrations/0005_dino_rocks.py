# Generated by Django 2.2.6 on 2020-01-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rock'),
    ]

    operations = [
        migrations.AddField(
            model_name='dino',
            name='rocks',
            field=models.ManyToManyField(to='main_app.Rock'),
        ),
    ]
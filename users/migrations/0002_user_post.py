# Generated by Django 4.0.6 on 2022-09-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharek', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.ManyToManyField(related_name='post', to='sharek.post'),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-02 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]

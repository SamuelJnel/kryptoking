# Generated by Django 3.2.8 on 2021-11-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
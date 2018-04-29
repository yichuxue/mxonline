# Generated by Django 2.0.4 on 2018-04-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='', max_length=300, verbose_name='课程须知'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-04-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='视频时长(分钟数)'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-04-15 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180414_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10, verbose_name='验证码类型'),
        ),
    ]

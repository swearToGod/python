# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srsys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='advert', verbose_name='广告图片(尺寸:325px*45px)')),
                ('advert_url', models.URLField(verbose_name='广告链接')),
                ('advert_num', models.IntegerField(verbose_name='广告序号')),
            ],
            options={
                'verbose_name': '广告',
                'verbose_name_plural': '广告',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '考生信息', 'verbose_name_plural': '考生分数'},
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postentry',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='blogphotos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='postentry',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='postentry',
            name='hero_image',
            field=models.ImageField(upload_to='blogphotos/%Y/%m/%d'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150405_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='hero_image',
            field=models.ImageField(upload_to='blog/static/blogphotos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='postentry',
            name='post_image',
            field=models.ImageField(upload_to='blog/static/blogphotos/%Y/%m/%d', blank=True),
        ),
    ]

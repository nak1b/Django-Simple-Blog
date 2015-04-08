# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150405_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='hero_image',
            field=models.ImageField(upload_to='blog/media/'),
        ),
        migrations.AlterField(
            model_name='postentry',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='blog/media/'),
        ),
    ]

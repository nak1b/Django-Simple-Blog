# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150407_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postentry',
            name='hero_image',
            field=models.ImageField(upload_to='/media/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150407_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='postentry',
            name='tags',
            field=models.ManyToManyField(to='blog.PostTag'),
        ),
    ]

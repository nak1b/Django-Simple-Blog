# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_body', models.TextField()),
                ('hero_image', models.ImageField(blank=True, upload_to='blogphotos/%Y/%m/%d')),
                ('author', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
    ]

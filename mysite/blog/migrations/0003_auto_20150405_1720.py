# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150405_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postentry',
            old_name='pub_date',
            new_name='created',
        ),
    ]

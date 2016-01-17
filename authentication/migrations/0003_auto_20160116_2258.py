# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20160116_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='updated_on',
            new_name='updated_at',
        ),
    ]

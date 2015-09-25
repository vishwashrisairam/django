# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150612_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=django_markdown.models.MarkdownField(),
            preserve_default=True,
        ),
    ]

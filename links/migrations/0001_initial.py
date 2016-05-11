# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 13:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата содания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ccылка',
                'verbose_name_plural': 'Ccылки',
            },
        ),
    ]

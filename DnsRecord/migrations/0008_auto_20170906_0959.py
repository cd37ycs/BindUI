# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-06 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DnsRecord', '0007_auto_20170906_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(blank=True, help_text='备注', max_length=255, null=True, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='record',
            name='primary_ns',
            field=models.CharField(blank=True, help_text='Primary name server for SOA record', max_length=255, null=True, verbose_name='primary_ns'),
        ),
        migrations.AlterField(
            model_name='record',
            name='resp_person',
            field=models.CharField(blank=True, help_text='Responsible person mail for SOA record', max_length=255, null=True, verbose_name='resp_person'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=255, verbose_name='zone')),
                ('host', models.CharField(blank=True, default=None, help_text='Host name or IP address', max_length=255, null=True, verbose_name='host')),
                ('type', models.CharField(blank=True, choices=[('A', 'A'), ('CNAME', 'CNAME'), ('MX', 'MX'), ('TXT', 'TXT'), ('NS', 'NS'), ('AAAA', 'AAAA'), ('SRV', 'SRV'), ('PTR', 'PTR'), ('SOA', 'SOA')], default=None, help_text='DNS data type', max_length=64, null=True, verbose_name='type')),
                ('data', models.CharField(help_text='IP address / Host name / Full domain name', max_length=255, verbose_name='data')),
                ('ttl', models.IntegerField(blank=True, default=None, help_text='Time to live', null=True, verbose_name='ttl')),
                ('mx_priority', models.CharField(blank=True, default=None, help_text='MX Priority', max_length=255, null=True, verbose_name='mx_priority')),
                ('refresh', models.IntegerField(blank=True, default=None, help_text='Refresh time for SOA record', null=True, verbose_name='refresh')),
                ('retry', models.IntegerField(blank=True, default=None, help_text='Retry time for SOA record', null=True, verbose_name='retry')),
                ('expire', models.IntegerField(blank=True, default=None, help_text='Expire time for SOA record', null=True, verbose_name='expire')),
                ('minimum', models.IntegerField(blank=True, default=None, help_text='Minimum time for SOA record', null=True, verbose_name='minimum')),
                ('serial', models.BigIntegerField(blank=True, default=None, help_text='serial # for SOA record', null=True, verbose_name='serial')),
                ('resp_person', models.CharField(blank=True, default=None, help_text='Responsible person mail for SOA record', max_length=255, null=True, verbose_name='resp_person')),
                ('primary_ns', models.CharField(blank=True, default=None, help_text='Primary name server for SOA record', max_length=255, null=True, verbose_name='primary_ns')),
                ('status', models.CharField(choices=[('on', '开启'), ('off', '暂停')], default='on', max_length=3, verbose_name='status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('comment', models.CharField(blank=True, default=None, help_text='备注', max_length=255, null=True, verbose_name='comment')),
            ],
        ),
        migrations.CreateModel(
            name='ZoneTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=255, verbose_name='zone name')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='注释')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='zone_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DnsRecord.ZoneTag'),
        ),
    ]
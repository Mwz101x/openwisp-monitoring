# Generated by Django 3.0.5 on 2020-05-27 03:06

import re
import uuid

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import swapper
from django.db import migrations, models

import openwisp_monitoring.device.base.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [('config', '0027_add_indexes_on_ip_fields')]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[],
            options={'proxy': True, 'indexes': [], 'constraints': []},
            bases=(
                openwisp_monitoring.device.base.models.AbstractDeviceData,
                swapper.get_model_name('config', 'Device'),
            ),
        ),
        migrations.CreateModel(
            name='DeviceMonitoring',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'status',
                    model_utils.fields.StatusField(
                        choices=[
                            ('unknown', 'unknown'),
                            ('ok', 'ok'),
                            ('problem', 'problem'),
                            ('critical', 'critical'),
                            ('deactivated', 'deactivated'),
                        ],
                        db_index=True,
                        default='unknown',
                        help_text='"unknown" means the device has been recently added; \n'
                        '"ok" means the device is operating normally; \n'
                        '"problem" means the device is having issues but it\'s still reachable; \n'
                        '"critical" means the device is not reachable or in critical conditions;\n'
                        '"deactivated" means the device is deactivated;',
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name='health status',
                    ),
                ),
                (
                    'device',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='monitoring',
                        to=swapper.get_model_name('config', 'Device'),
                    ),
                ),
                (
                    'details',
                    models.CharField(default='devicemonitoring', max_length=64),
                ),
            ],
            options={'abstract': False},
        ),
        migrations.CreateModel(
            name='WifiClient',
            fields=[
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'mac_address',
                    models.CharField(
                        db_index=True,
                        help_text='MAC address',
                        max_length=17,
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'),
                                code='invalid',
                                message='Must be a valid mac address.',
                            )
                        ],
                    ),
                ),
                ('vendor', models.CharField(blank=True, max_length=200, null=True)),
                (
                    'ht',
                    models.BooleanField(
                        blank=True, default=None, null=True, verbose_name='HT'
                    ),
                ),
                (
                    'vht',
                    models.BooleanField(
                        blank=True, default=None, null=True, verbose_name='VHT'
                    ),
                ),
                (
                    'he',
                    models.BooleanField(
                        blank=True, default=None, null=True, verbose_name='HE'
                    ),
                ),
                ('wmm', models.BooleanField(default=False, verbose_name='WMM')),
                ('wds', models.BooleanField(default=False, verbose_name='WDS')),
                ('wps', models.BooleanField(default=False, verbose_name='WPS')),
                (
                    'details',
                    models.CharField(default='devicemonitoring', max_length=64),
                ),
            ],
            options={
                'verbose_name': 'WiFi Client',
                'abstract': False,
                # To prevent DRF UnorderedObjectListWarning in pagination
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='WifiSession',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'ssid',
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name='SSID'
                    ),
                ),
                ('interface_name', models.CharField(max_length=15)),
                (
                    'start_time',
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name='start time'
                    ),
                ),
                (
                    'stop_time',
                    models.DateTimeField(
                        blank=True, db_index=True, null=True, verbose_name='stop time'
                    ),
                ),
                (
                    'details',
                    models.CharField(default='devicemonitoring', max_length=64),
                ),
                (
                    'device',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('config', 'Device'),
                    ),
                ),
                (
                    'wifi_client',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='sample_device_monitoring.wificlient',
                    ),
                ),
            ],
            options={
                'verbose_name': 'WiFi Session',
                'abstract': False,
                'ordering': ('-start_time',),
            },
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-31 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoredEventRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('application_name', models.CharField(max_length=32)),
                ('originator_id', models.UUIDField()),
                ('originator_version', models.BigIntegerField()),
                ('topic', models.TextField()),
                ('state', models.BinaryField()),
            ],
            options={
                'db_table': 'stored_events',
                'unique_together': {('application_name', 'id'), ('application_name', 'originator_id', 'originator_version')},
            },
        ),
        migrations.CreateModel(
            name='SnapshotRecord',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('application_name', models.CharField(max_length=32)),
                ('originator_id', models.UUIDField()),
                ('originator_version', models.BigIntegerField()),
                ('topic', models.TextField()),
                ('state', models.BinaryField()),
            ],
            options={
                'db_table': 'snapshots',
                'unique_together': {('application_name', 'originator_id', 'originator_version')},
            },
        ),
        migrations.CreateModel(
            name='NotificationTrackingRecord',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('application_name', models.CharField(max_length=32)),
                ('upstream_application_name', models.CharField(max_length=32)),
                ('notification_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'notification_tracking',
                'unique_together': {('application_name', 'upstream_application_name', 'notification_id')},
            },
        ),
    ]

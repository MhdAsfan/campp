# Generated by Django 3.2.22 on 2024-02-29 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(db_column='Status_id', primary_key=True, serialize=False)),
                ('check_id', models.CharField(db_column='Check_id', max_length=45)),
                ('count_id', models.CharField(blank=True, db_column='Count_id', max_length=45, null=True)),
                ('date_time_id', models.CharField(blank=True, max_length=45, null=True)),
                ('paper_availability', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
        ),
    ]

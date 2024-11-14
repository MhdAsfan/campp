# Generated by Django 3.2.22 on 2024-03-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignPaper',
            fields=[
                ('assign_paper_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'assign_paper',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssuePaper',
            fields=[
                ('work_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'issue_paper',
                'managed': False,
            },
        ),
    ]
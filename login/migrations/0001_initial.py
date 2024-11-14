# Generated by Django 3.2.22 on 2024-02-29 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_collation='latin1_bin', max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('uid', models.IntegerField()),
            ],
            options={
                'db_table': 'issuepaper',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.2.7 on 2021-11-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('link_zoom', models.CharField(max_length=120, null=True)),
                ('id_meeting', models.CharField(max_length=30, null=True)),
                ('password_meeting', models.CharField(max_length=10, null=True)),
                ('record_zoom', models.CharField(blank=True, max_length=120, null=True)),
                ('password_record', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-27 02:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('std', models.CharField(choices=[('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True)),
                ('link', models.URLField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('Incomplete', 'Incomplete'), ('Concluded', 'Concluded'), ('Deleted', 'Deleted')], default='Incomplete', max_length=40, null=True)),
                ('time', models.TimeField(null=True)),
                ('participents', models.ManyToManyField(blank=True, to='users.Student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.subject')),
            ],
        ),
    ]

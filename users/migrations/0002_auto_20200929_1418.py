# Generated by Django 3.1.1 on 2020-09-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='otp',
            field=models.SmallIntegerField(null=True),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

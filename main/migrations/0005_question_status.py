# Generated by Django 3.1.2 on 2020-10-05 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201005_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.TextField(choices=[('Unanswered', 'Unanswered'), ('Answered', 'Answered')], default='Unanswered', null=True),
        ),
    ]
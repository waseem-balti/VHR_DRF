# Generated by Django 5.1.6 on 2025-03-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0010_interview_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0008_remove_applicantresponse_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supper', '0002_day_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]

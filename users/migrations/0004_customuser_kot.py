# Generated by Django 2.1.1 on 2018-09-01 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_kot'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='kot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Kot'),
        ),
    ]

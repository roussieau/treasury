# Generated by Django 2.1.1 on 2018-09-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_treasurer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
    ]

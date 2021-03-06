# Generated by Django 2.1.1 on 2018-09-02 13:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.Expense'),
        ),
    ]

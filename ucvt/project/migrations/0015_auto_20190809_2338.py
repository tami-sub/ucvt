# Generated by Django 2.1.3 on 2019-08-09 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20190809_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_payment_fact_when',
            field=models.DateField(default='2000-01-01', null=True, verbose_name=''),
        ),
    ]
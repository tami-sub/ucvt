# Generated by Django 2.1.3 on 2019-08-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20190809_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_payment_fact_how_much',
            field=models.IntegerField(default=0, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_payment_fact_where',
            field=models.CharField(default='Не указано', max_length=100, null=True, verbose_name=''),
        ),
    ]

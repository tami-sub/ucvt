# Generated by Django 2.1.3 on 2019-08-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20190809_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_contract_fact',
            field=models.CharField(default='Не был', max_length=20, null=True),
        ),
    ]

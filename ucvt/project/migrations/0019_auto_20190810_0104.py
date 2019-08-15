# Generated by Django 2.1.3 on 2019-08-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20190810_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_got_info',
            field=models.CharField(choices=[('Написал мне', 'Написал мне'), ('От меня', 'От меня'), ('По объявлению', 'По объявлению')], max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

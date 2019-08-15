# Generated by Django 2.1.3 on 2019-08-09 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190807_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_contact_fact_academy',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='message_manager',
            name='message_from',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'managers'}, null=True, on_delete='', related_name='send_letter_manager', to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='message_manager',
            name='message_to_back',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'managers'}, null=True, on_delete='', related_name='got_letter_manager_back', to=settings.AUTH_USER_MODEL),
        ),
    ]
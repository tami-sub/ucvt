# Generated by Django 2.1.3 on 2019-08-07 13:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_to',
            field=models.ForeignKey(default=-1, limit_choices_to={'groups__name': 'uppermanagers'}, on_delete='', related_name='got_letter', to=settings.AUTH_USER_MODEL),
        ),
    ]

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Partner (models.Model):
    class Meta:
        db_table = "partner"
    partner_surname = models.CharField(verbose_name="",max_length=100)
    partner_name = models.CharField(verbose_name="", max_length=100)
    partner_patronymic = models.CharField(verbose_name="",max_length=100)
    partner_email = models.EmailField(verbose_name="",null=False, max_length=100)
    partner_number = models.BigIntegerField(verbose_name="",null=False)
    partner_free_info = models.TextField(verbose_name="")
    partner_user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)
    partner_status = models.BooleanField(verbose_name="",default=False)
class Customer (models.Model):
    class Meta:
        db_table = "customer"
    customer_register_date = models.DateField(auto_now_add=True)

    CHOICES = (
                ('Написал мне', 'Написал мне'),
                ('От меня', 'От меня'),
                ('По объявлению', 'По объявлению')
            )
    customer_got_info = models.CharField(verbose_name="", max_length=20, choices=CHOICES)
    customer_surname = models.CharField(verbose_name="", max_length=100)
    customer_name = models.CharField(verbose_name="", max_length=100)
    customer_patronymic = models.CharField(verbose_name="", max_length=100)
    customer_form_academy = models.CharField(verbose_name="", max_length=100)
    customer_about_comments = models.TextField(verbose_name="", max_length=100)
    customer_partner = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)


    customer_contact_fact_academy = models.CharField(verbose_name="",max_length=20, default="Нет", null=True)
    customer_contract_fact = models.CharField(verbose_name="",max_length=20, default="Нет", null=True)
    customer_payment_fact_when = models.DateField(verbose_name="",null=True)
    customer_payment_fact_where = models.CharField(verbose_name="", default="Не указано",max_length=100, null=True)
    customer_payment_fact_how_much = models.IntegerField(verbose_name="", default=0, null=True)

    customer_remove = models.BooleanField(default=False)

class Message (models.Model):
    class Meta:
        db_table = "message"

    message_text = models.TextField(max_length=200)
    message_from = models.ForeignKey(User, verbose_name="", limit_choices_to={'groups__name': "partners"}, on_delete=models.CASCADE,
                                     null=True, related_name="send_letter")
    message_to = models.ForeignKey(User, limit_choices_to={'groups__name': "uppermanagers"}, on_delete=models.CASCADE, null=True,
                                   related_name="got_letter")

    message_from_back = models.ForeignKey(User, verbose_name="", null=True,
                                          limit_choices_to={'groups__name': "uppermanagers"}, on_delete=models.CASCADE,
                                          related_name="send_letter_back")
    message_to_back = models.ForeignKey(User, null=True, limit_choices_to={'groups__name': "partners"}, on_delete=models.CASCADE,
                                        related_name="got_letter_back")
    message_date = models.DateTimeField(auto_now=True)

class Message_manager (models.Model):
    class Meta:
        db_table = "message_manager"

    message_text = models.TextField(max_length=200)
    message_from = models.ForeignKey(User, verbose_name="", limit_choices_to={'groups__name': "managers"},
                                         on_delete=models.CASCADE,
                                         null=True, related_name="send_letter_manager")
    message_to = models.ForeignKey(User, limit_choices_to={'groups__name': "uppermanagers"}, on_delete=models.CASCADE,
                                       null=True,
                                       related_name="got_letter_manager")

    message_from_back = models.ForeignKey(User, verbose_name="", null=True,
                                              limit_choices_to={'groups__name': "uppermanagers"}, on_delete=models.CASCADE,
                                              related_name="send_letter_manager_back")
    message_to_back = models.ForeignKey(User, null=True, limit_choices_to={'groups__name': "managers"},
                                            on_delete=models.CASCADE,
                                            related_name="got_letter_manager_back")
    message_date = models.DateTimeField(auto_now=True)
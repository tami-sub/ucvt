from django.forms import ModelForm, forms, Textarea, Select, TextInput, EmailField, NumberInput
from .models import Partner, Customer, Message, Message_manager

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['partner_surname','partner_name','partner_patronymic', 'partner_email', 'partner_number', 'partner_free_info']
        widgets = {
            'partner_surname': TextInput(attrs={'placeholder': "Фамилия"}),
            'partner_name': TextInput(attrs={'placeholder': "Имя"}),
            'partner_patronymic': TextInput(attrs={'placeholder': "Отчество"}),
            'partner_email': TextInput(attrs={'placeholder': "Электронная почта"}),
            'partner_number': NumberInput(attrs={'placeholder': "Номер телефона"}),
            'partner_free_info': Textarea(attrs={'placeholder': "Ваш комментарий"}),

        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_surname','customer_name','customer_patronymic', 'customer_got_info', 'customer_form_academy', 'customer_about_comments']
        widgets = {
            'customer_surname': TextInput(attrs={'placeholder': "Фамилия"}),
            'customer_name': TextInput(attrs={'placeholder': "Имя"}),
            'customer_patronymic': TextInput(attrs={'placeholder': "Отчество"}),
            'customer_form_academy': TextInput(attrs={'placeholder': "Форма контакта"}),
            'customer_about_comments': Textarea(attrs={'placeholder': "Комментарий"}),

        }
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_from','message_to', 'message_text']
        widgets = {
            'message_from': Select(attrs={'style': """display: none"""}),
        }

class MessageFormBack(ModelForm):
    class Meta:
        model = Message
        fields = ['message_from_back','message_to_back', 'message_text']
        widgets = {
            'message_from_back': Select(attrs={'style': """display: none"""}),
        }

class MessageManagerForm(ModelForm):
    class Meta:
        model = Message_manager
        fields = ['message_from','message_to', 'message_text']
        widgets = {
            'message_from': Select(attrs={'style': """display: none"""}),
        }
class MessageManagerFormBack(ModelForm):
    class Meta:
        model = Message_manager
        fields = ['message_from_back', 'message_to_back', 'message_text']
        widgets = {
            'message_from_back': Select(attrs={'style': """display: none"""}),
        }

# class Customer_Payment_Fact_When(ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['customer_payment_fact_when']
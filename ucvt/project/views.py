from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, render_to_response, Http404, HttpResponseRedirect
from project.models import Partner, Customer, Message, Message_manager
from django.core.exceptions import ObjectDoesNotExist
from .forms import PartnerForm, CustomerForm,MessageForm, MessageFormBack, MessageManagerForm,MessageManagerFormBack
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from itertools import chain
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    user = auth.get_user(request)


    if (user in Group.objects.get(name="uppermanagers").user_set.all()):
        args['uppermanagers'] = Group.objects.get(name="uppermanagers").user_set.all()


    elif (user in Group.objects.get(name="managers").user_set.all()):
        args['managers'] = Group.objects.get(name="managers").user_set.all()


    elif(user in Group.objects.get(name="partners").user_set.all()):
        args['partners'] = Group.objects.get(name="partners").user_set.all()


    else:
        args['void'] = "void"


    return render(request, 'home.html', args)

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    args['zorro'] = PartnerForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        form = PartnerForm(request.POST)
        email = request.POST.get('partner_email')
        if newuser_form.is_valid() and form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            newuser.is_active = False
            newuser.email = request.POST.get('partner_email')
            newuser.last_name = request.POST.get('partner_surname')
            newuser.first_name = request.POST.get('partner_name')
            newuser.save()

            group = Group.objects.get(name="partners")

            user = User.objects.get(id=newuser.id)
            user.groups.add(group)

            partner = form.save(commit=False)
            partner.partner_user = User.objects.get(id=newuser.id)
            form.save()

            uppermanagers = User.objects.filter(groups__name="uppermanagers")
            recipient_list = []
            for i in uppermanagers:
                recipient_list.append(i.email)
            send_mail("UCVT", "Требуется одобрить нового партнёра", 'bokabokajoka@gmail.com', recipient_list)

            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
            args['zorro'] = form
    return render_to_response('register.html', args)

def add_client(request):

    args = {}
    args.update(csrf(request))
    user_id = auth.get_user(request).id
    args['form'] = CustomerForm()
    args['username'] = auth.get_user(request).username
    args['oga'] = Customer.objects.filter(customer_partner=user_id, customer_remove=False)

    if request.POST:
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():

            customer = customer_form.save(commit=False)
            customer.customer_partner = User.objects.get(id=user_id)
            customer.customer_payment_fact_when = "0001-01-01"
            customer.save()

        else:
            args['form'] = CustomerForm()

    return render_to_response('addclient.html', args)

def status(request, customer_id):

    current = Customer.objects.get(id=customer_id)
    current.customer_remove = True
    current.save()

    return redirect('addclient')


def choice(request, choice=0):
    kekus = redirect("/dialog/")
    kekus.set_cookie("choice", choice)
    return kekus


def dialog(request, got_id=-1):
    args = {}
    args.update(csrf(request))
    users_in_uppermanagers = Group.objects.get(name="uppermanagers").user_set.all()
    users_in_managers = Group.objects.get(name="managers").user_set.all()

    choice = int(request.COOKIES.get("choice", 0))

    if (auth.get_user(request) in users_in_uppermanagers):

        if (choice == 0):
            groups_name = "partners"
            args['message'] = MessageFormBack(initial={'message_from_back': request.user.id})
            if request.POST:
                message_form = MessageFormBack(request.POST)
                if message_form.is_valid():
                    message_form.save()


            message_from = Message.objects.filter(message_from_back=auth.get_user(request).id, message_to_back=got_id)
            message_to = (Message.objects.filter(message_from=got_id, message_to=auth.get_user(request).id))
            result = list(chain(message_from, message_to))
            result = sorted(result, key=lambda instance: instance.message_date)

        elif (choice == 1):

            groups_name = "managers"
            args['message'] = MessageManagerFormBack(initial={'message_from_back': request.user.id})
            if request.POST:
                message_form = MessageManagerFormBack(request.POST)
                if message_form.is_valid():
                    message_form.save()

            message_from = Message_manager.objects.filter(message_from_back=auth.get_user(request).id, message_to_back=got_id)
            message_to = (Message_manager.objects.filter(message_from=got_id, message_to=auth.get_user(request).id))
            result = list(chain(message_from, message_to))
            result = sorted(result, key=lambda instance: instance.message_date)




        args['uppermanagers'] = users_in_uppermanagers
    elif (auth.get_user(request) in users_in_managers):

        args['message'] = MessageManagerForm(initial={'message_from': request.user.id})
        groups_name = 'uppermanagers'

        if request.POST:
                message_form = MessageManagerForm(request.POST)
                if message_form.is_valid():
                    message_form.save()

        message_from = Message_manager.objects.filter(message_from=auth.get_user(request).id, message_to =got_id)
        message_to = (Message_manager.objects.filter(message_from_back=got_id, message_to_back =auth.get_user(request).id))
        result = list(chain(message_from, message_to))
        result = sorted(result, key=lambda instance: instance.message_date)

    else:
        args['message'] = MessageForm(initial={'message_from': request.user.id})
        groups_name = 'uppermanagers'
        if request.POST:
                message_form = MessageForm(request.POST)
                if message_form.is_valid():
                    message_form.save()

        message_from = Message.objects.filter(message_from=auth.get_user(request).id, message_to = got_id)
        message_to = (Message.objects.filter(message_from_back=got_id, message_to_back =auth.get_user(request).id))
        result = list(chain(message_from, message_to))
        result = sorted(result, key=lambda instance: instance.message_date)


    args['from'] = result
    args['username'] = auth.get_user(request).username
    args['to'] = User.objects.filter(groups__name=groups_name)


    return render(request, 'dialog.html', args)

def customers(request, command=0):
    args = {}
    args.update(csrf(request))
    user = auth.get_user(request)
    args['username'] = user
    if (user in (Group.objects.get(name="managers").user_set.all())):
        args['all_managers'] = Group.objects.get(name="managers").user_set.all()
    elif (user in (Group.objects.get(name="uppermanagers").user_set.all())):
        args['all_managers'] = Group.objects.get(name="uppermanagers").user_set.all()
    filter = Customer.objects.all()
    list = { 0:  sorted(filter, key=lambda instance: instance.customer_register_date),
             1:  sorted(filter, key=lambda instance: instance.customer_register_date),
             10: sorted(filter, key=lambda instance: instance.customer_surname),
             11: sorted(filter, key=lambda instance: instance.customer_surname),
             20: sorted(filter, key=lambda instance: instance.customer_name),
             21: sorted(filter, key=lambda instance: instance.customer_name),
             30: sorted(filter, key=lambda instance: instance.customer_patronymic),
             31: sorted(filter, key=lambda instance: instance.customer_patronymic),
             40: sorted(filter, key=lambda instance: instance.customer_got_info),
             41: sorted(filter, key=lambda instance: instance.customer_got_info),
             50: sorted(filter, key=lambda instance: instance.customer_form_academy),
             51: sorted(filter, key=lambda instance: instance.customer_form_academy),
             60: sorted(filter, key=lambda instance: instance.customer_contact_fact_academy),
             61: sorted(filter, key=lambda instance: instance.customer_contact_fact_academy),
             70: sorted(filter, key=lambda instance: instance.customer_contract_fact),
             71: sorted(filter, key=lambda instance: instance.customer_contract_fact),
             80: sorted(filter, key=lambda instance: instance.customer_payment_fact_when),
             81: sorted(filter, key=lambda instance: instance.customer_payment_fact_when),
             90: sorted(filter, key=lambda instance: instance.customer_payment_fact_where),
             91: sorted(filter, key=lambda instance: instance.customer_payment_fact_where),
             100: sorted(filter, key=lambda instance: instance.customer_payment_fact_how_much),
             101: sorted(filter, key=lambda instance: instance.customer_payment_fact_how_much)
             }
    if (list[int(command)] is not None):
        if (int(command) % 2 == 0):
            filter = reversed(list[int(command)])
        elif(int(command) % 2 != 0):
            filter = list[int(command)]

    args['customers'] = filter
    return render(request, 'customers.html', args)

def customer_contact_fact_academy(request, customer_id):
    current = Customer.objects.get(id=customer_id)
    if (current.customer_contact_fact_academy != "Да"):
        current.customer_contact_fact_academy = "Да"
        current.save()
    else:
        current.customer_contact_fact_academy = "Нет"
        current.save()
    return redirect("/customers/")


def customer_contract_fact(request, customer_id):
    current = Customer.objects.get(id=customer_id)
    if (current.customer_contract_fact != "Да"):
        current.customer_contract_fact = "Да"
        current.save()
    else:
        current.customer_contract_fact = "Нет"
        current.save()
    return redirect("/customers/")

def customer_payment_fact_when(request, customer_id):
    current = Customer.objects.get(id=customer_id)
    if request.POST:
        current.customer_payment_fact_when = request.POST.get('customer_payment_fact_when')
        current.save()
    return redirect("/customers/")

def customer_payment_fact_where(request, customer_id):
    current = Customer.objects.get(id=customer_id)
    if request.POST:
        current.customer_payment_fact_where = request.POST.get('customer_payment_fact_where')
        current.save()
    return redirect("/customers/")

def customer_payment_fact_how_much(request, customer_id):
    current = Customer.objects.get(id=customer_id)
    if request.POST:
        current.customer_payment_fact_how_much = int(request.POST.get('customer_payment_fact_how_much'))
        current.save()
    return redirect("/customers/")


def partners(request, partner_id = -1):
    args = {}
    args.update(csrf(request))
    user = auth.get_user(request)
    args['username'] = user
    if (user in (Group.objects.get(name="managers").user_set.all())):
        args['all_managers'] = Group.objects.get(name="managers").user_set.all()
    elif (user in (Group.objects.get(name="uppermanagers").user_set.all())):
        args['all_managers'] = Group.objects.get(name="uppermanagers").user_set.all()

    if (int(partner_id) > 0):
        current_partner = Partner.objects.get(partner_user_id=partner_id)
        current_auth_partner = User.objects.get(id=partner_id)
        if (current_partner.partner_status == False):
            current_partner.partner_status = True
            current_partner.save()
            current_auth_partner.is_active = True
            current_auth_partner.save()
            send_mail("UCVT", "ВАС ОДОБРИЛИ", 'bokabokajoka@gmail.com', [current_auth_partner.email])

    args['partners'] = Partner.objects.all()
    return render(request, 'partners.html', args)

def partners_remove(request,partner_id = -1):
    current_partner = Partner.objects.get(partner_user_id=partner_id)
    current_group_partner = Group.objects.get(user=partner_id)
    current_user_partner = User.objects.get(id=partner_id)
    if (User.objects.get(id=partner_id).is_active == False):
        current_partner.delete()
        current_group_partner.user_set.remove()
        send_mail("UCVT", "ВАС НЕ ОДОБРИЛИ", 'bokabokajoka@gmail.com', [current_user_partner.email])
        current_user_partner.delete()
    else:
        if(Customer.objects.filter(customer_partner_id=partner_id).exists()):

            current_customer_partner = Customer.objects.filter(customer_partner_id=partner_id)
            current_customer_partner.delete()
        if(Message.objects.filter(message_from_id=partner_id).exists()):

            current_message_partner_1 = Message.objects.filter(message_from_id=partner_id)
            current_message_partner_1.delete()
        if(Message.objects.filter(message_to_back_id = partner_id)):
            current_message_partner_2 = Message.objects.filter(message_to_back_id = partner_id)
            current_message_partner_2.delete()

        current_partner.delete()
        current_group_partner.delete()
        current_user_partner.delete()

    return redirect("/partners/")

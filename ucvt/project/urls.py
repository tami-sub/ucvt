from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="name"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('addclient/', views.add_client, name="addclient"),
    path('dialog/', views.dialog, name="dialog"),
    path('customers/', views.customers, name="customers"),
    path('partners/', views.partners, name="partners"),


    re_path(r'^status/(?P<customer_id>\d+)/', views.status),
    re_path(r'^dialog/(?P<got_id>\d+)/', views.dialog),
    re_path(r'^choice/(?P<choice>\d+)/', views.choice),
    re_path(r'^customer_contact_fact_academy/(?P<customer_id>\d+)/', views.customer_contact_fact_academy),
    re_path(r'^customer_contract_fact/(?P<customer_id>\d+)/', views.customer_contract_fact),

    re_path(r'^customer_payment_fact_when/(?P<customer_id>\d+)/', views.customer_payment_fact_when),
    re_path(r'^customer_payment_fact_where/(?P<customer_id>\d+)/', views.customer_payment_fact_where),
    re_path(r'^customer_payment_fact_how_much/(?P<customer_id>\d+)/', views.customer_payment_fact_how_much),

    re_path(r'^customers/(?P<command>\d+)/', views.customers),
    re_path(r'^partners/(?P<partner_id>\d+)/', views.partners),
re_path(r'^partners_remove/(?P<partner_id>\d+)/', views.partners_remove)






]


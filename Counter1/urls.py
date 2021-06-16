from django.urls import path
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [ 
    path('clients', views.clients_list),
    path('sms/', views.sms),
    path('sms/<int:pk>', views.smsDetail),

    path("update/<str:pk>", views.updateBilling),
    path("detail/<str:pk>", views.billingDetail),
    path("create", views.billingCreate),
    path("delete/<str:pk>", views.deleteBilling),
    
    path("customer", views.createCustomer),
    path("list/<str:pk>", views.singleView),
    path("all", views.listView),
    path("blacklist/<str:pk>", views.blacklist),
    path("whitelist/<str:pk>", views.whitelist),
    path("AddMessage", views.AddMessage),
    path("allM", views.listMessage),

    path("loan/<int:id>", views.loan_approval_message),
    path("dd/<int:pk>", views.due_date_message),
    path("name_message/<str:pk>", views.name_message),
    path("id/<str:pk>", views.installment_date_message),
    path("an/<str:pk>", views.account_number_message),
    path("lb/<str:pk>", views.loan_balance_message),
    path("pn/<str:pk>", views.payBill_number_message),
    path("tn/<str:pk>", views.tenant_name_message),
    path("sa/<str:pk>", views.saving_amount_message),
    path("af/<str:pk>", views.admin_fee_message),
    path("np/<str:pk>", views.new_pin_message),

]

urlpatterns = format_suffix_patterns(urlpatterns)
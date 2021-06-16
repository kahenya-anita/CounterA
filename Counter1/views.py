
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *

#CLIENT
@api_view(['GET', 'POST'])
def clients_list(request):
    if request.method == 'GET':
        clients = Clients.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientsSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def loan_approval_message(request,id):
    message=None
    loan_limit=9
    
    message=ClientsSMS(client_id=id,message_type_id='2').message
    
    # message2=message.replace("%LL",str(loan_limit))
    return Response({'message':message})

@api_view()
def due_date_message(message_id,Due_Date):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%DD",Due_Date)
    return message

@api_view()
def name_message(message_id,Name):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%FN",Name)
    return message

@api_view()
def installment_date_message(message_id,Installment_Date):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%ID", Installment_Date)
    return message

@api_view()
def account_number_message(message_id,Account_Number):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%AN", Account_Number)
    return message

@api_view()
def loan_balance_message(message_id,Loan_Balance):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%LB", Loan_Balance)
    return message

@api_view()
def payBill_number_message(message_id,PayBill_Number):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%PN", PayBill_Number)
    return message

@api_view()
def tenant_name_message(message_id,Tenant_Name):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%TN", Tenant_Name)
    return message

@api_view()
def saving_amount_message(message_id,Saving_Amount):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%SA", Saving_Amount)
    return message

@api_view()
def admin_fee_message(message_id,Admin_Fee):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%AF", Admin_Fee)
    return message

@api_view()
def new_pin_message(message_id,New_Pin):
    message=None
    c=ClientsSMS(Client_id=Clients,MessageType_id=message_id)
    message=c.message
    message.replace("%NP", New_Pin)
    return message


@api_view(['POST'])
def AddMessage(request):    
    serializer = ClientsSMSSerializer(data=request.data)
    if serializer.is_valid():
        Message=serializer.data['message']
        message_type=serializer.data['message_type']        
        client=serializer.data['client']   
        try:
            c=ClientsSMS(client_id=client,message_type_id=message_type)
            c.Message=Message
            c.save()
            
                
            return Response({'Success': 'True', 'Code': 200,'message': 'Successful'},
                    status=status.HTTP_200_OK)
        except ObjectDoesNotExist:

            slider=ClientsSMS(
                message=Message,
                client=client,
                message_type_id=message_type
                )
            slider.save()
            return Response({'Success': 'True', 'Code': 200,'message': 'Successful'},
                status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listMessage(request):
    SMS = ClientsSMS.objects.all()
    serializer = ClientsSMSSerializer(SMS, many=True)
    return Response(serializer.data,  status=status.HTTP_200_OK)

#SMS
@api_view(['POST'])
def sms(request):
    serializer = ClientsSMSSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def smsDetail(request, pk): 
    sms = ClientsSMS.objects.get(id=pk)
    serializer = ClientsSMSSerializer(sms, many=False)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


#BILLING
@api_view(['POST'])
def billingCreate(request): 
    serializer = BillingSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def billingDetail(request, pk): 
    billings = Billing.objects.get(id=pk)
    serializer = BillingSerializer(billings, many=False)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def updateBilling(request, pk):
        billings = Billing.objects.get(id=pk)
        serializer = BillingSerializer(instance=billings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)
   
@api_view(['DELETE'])
def deleteBilling(request, pk):
        billings = Billing.objects.get(id=pk)
        billings.delete()
        return Response("Bill deleted successfuly!", status=status.HTTP_410_GONE)


# Customer Model  
@api_view(['POST'])
def createCustomer(request): 
    serializer = CustomersSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def singleView(request, pk): 
    customer = Customers.objects.get(id=pk)
    serializer = CustomersSerializer(customer, many=False)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def listView(request): 
    customer = Customers.objects.all()
    serializer = CustomersSerializer(customer, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view()
def blacklist(request, pk): 
    customer = Customers.objects.get(id=pk)
    customer.blacklist = True
    customer.save()
    return Response({"Blacklisted sucessfully!"})

@api_view()
def whitelist(request, pk): 
    customer = Customers.objects.get(id=pk)
    customer.whitelist = True
    customer.save()
    return Response({"Whitelisted sucessfully!"})


#LOANS
#@api_view(['PATCH'])
#def loanLimit(request, pk):
    #customer = Customers.objects.filter(pk=pk).first()
    #data = request.data
    #customer.loan_limit = data['loan_limit']
    #serializer = CustomersSerializer(customer)
    #if serializer.is_valid():
            #serializer.save()
    #return Response({"message":"Loan limit updated successfully"})










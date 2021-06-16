from django.db import models



class MessageType(models.Model):
    message_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.message_type 

class Clients(models.Model):
    company_name = models.CharField(max_length=225)
    client_name = models.CharField(max_length=225)
    address = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,unique=True) 
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12,unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)
    modules = models.CharField(max_length=15000,blank=True)
    package = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    officer_types = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.client_name


class ClientsSMS(models.Model):
    message = models.CharField(max_length=1000)
    message_type = models.ForeignKey(MessageType, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.message_type


class CustomSMS(models.Model):
    message = models.CharField(max_length=1000)
    message_type = models.ForeignKey(MessageType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.message_type

class Billing(models.Model):
    min_amount=models.DecimalField( max_digits=5, decimal_places=2, default=0)
    billing_rates=models.DecimalField( max_digits=5, decimal_places=2, default=0)
    grace_period=models.IntegerField(default=0 )
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.min_amount

class Customers(models.Model):
    
    email_address = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    loan_type = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    physical_address = models.CharField(max_length=100, blank=True, null=True)
    applicant_address = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=100, blank=True, null=True)
    dependents = models.CharField(max_length=100, blank=True, null=True)
    device_name = models.CharField(max_length=100, blank=True, null=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    uniqueid = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    registration_fee = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.0)
    sharecapital_amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.0)
    membership_number = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=100)
    pin = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    upload_type = models.CharField(max_length=100, blank=True, null=True)
    id_front = models.CharField(max_length=1000, blank=True, null=True)
    gender = models.CharField(max_length=1000, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    id_back = models.CharField(max_length=1000, blank=True, null=True)
    loan_limit = models.CharField(max_length=100, blank=True, null=True)
    automatic = models.BooleanField(default=False)
    action_by = models.CharField(max_length=100, blank=True, null=True)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    otp = models.CharField(max_length=100, blank=True, null=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, blank=True, null=True)
    blacklist = models.BooleanField(default=False)
    first_verification = models.CharField(
        max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.firstname 


    
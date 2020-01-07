from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.conf import settings
from .models import Customer, Product
from django.views.generic import ListView
import random
import string
import json


def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def contact(request):

    if request.method == 'GET':

        name = request.GET.get('name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        landmark = request.GET.get('landmark')
        address = request.GET.get('address')
        order_id_gen=random_string_generator()
        prod = Product.objects.all()
        # customer_details = Customer.objects.create(
        #     name=name, email=email, mobile=phone,
        #     landmark=landmark, address=address,
        # )
        # if likedpost:
        #     from_email = settings.EMAIL_HOST_USER
        #     recipient_list = [email]
        #     send_mail(
        #         'CompanyName Laundry Service',
        #         ' Hi, ' + name +
        #         '\n Thank you for choosing us your reference id is ' + order_id_gen +
        #         '\n We are processing your request and our team will contact you soon.',
        #         from_email,
        #         recipient_list, fail_silently=False
        # 
    return render(request, 'app1/base.html', {'prod': prod})
    

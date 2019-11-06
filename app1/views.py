from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app1.models import LaundryModel
from django.core.mail import send_mail
from django.conf import settings
import random
import string


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

        likedpost = LaundryModel.objects.create(
            name=name, email=email, mobile=phone,
            landmark=landmark, address=address,
            order_id=order_id_gen
        )
        if likedpost:
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(
                'CompanyName Laundry Service',
                ' Hi, ' + name +
                '\n Thank you for choosing us your reference id is ' + order_id_gen +
                '\n We are processing your request and our team will contact you soon.',
                from_email,
                recipient_list, fail_silently=False
            )
        return HttpResponse(
            "Success"
        )
    else:
        return HttpResponse(
            "Oops something weent wrong!!!!"
        )
        
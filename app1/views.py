from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random
import string


def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def contact(request):
    product = Product.objects.all()
    return render(request, 'app1/base.html', {'product': product})

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import LaundryModel
from django.core.mail import send_mail
from django.conf import settings


def likepost(request):
    import ipdb; ipdb.set_trace()
    if request.method == 'GET':
            name = request.GET['name']
            email = request.GET['email']
            phone = request.GET['phone']
            landmark = request.GET['landmark']
            address = request.GET['address']

            likedpost = LaundryModel.objects.create(
                name=name, email=email, mobile=phone,
                landmark=landmark, address=address
            )
            if likedpost:
                recipient_list = ['jigaved765@mail8app.com',]
                send_mail(
                    'Thank you for registering to our site',
                    ' it  means a world to us ',
                    'ankurwave09@gmail.com', ['jigaved765@mail8app.com',],
                    fail_silently=False
                )
                
            return HttpResponse(
                "Success and mail is sent on your given email id"
            )
    else:
            return HttpResponse(
                "Oops data not saved pls try again!!!!"
            )
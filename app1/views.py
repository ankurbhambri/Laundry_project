from django.shortcuts import render
from django.http import HttpResponse
from app1.models import LaundryModel
from django.views.generic import TemplateView


def likepost(request):
    import ipdb; ipdb.set_trace()
    if request.method == 'GET':
            name = request.GET['name']
            email = request.GET['email']
            phone = request.GET['phone']
            landmark = request.GET['landmark']
            address = request.GET['address']

            likedpost = Post.obejcts.create(
                name=name, email=email, phone=phone,
                landmark=landmark, address=address
            )
            return HttpResponse("Success!")
    else:
            return HttpResponse("Oops data not saved pls try again!!!!")
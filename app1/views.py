from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Customer, Product
from .forms import PostForm
import random
import string


def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def contact(request):
    product = Product.objects.all()
    return render(request, 'app1/base.html', {'product': product})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app1/base.html', {'form': form})
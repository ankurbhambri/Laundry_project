from django.urls import path
from django.views.generic import TemplateView
from app1 import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="app1/index.html")),
    path('likepost/', views.likepost, name='likepost'),
]
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('test/' , views.test , name='test'),
    path('about/' , views.about , name='about'),
    path('contact/' , views.contact , name='contact'),
    path('elements/' , views.elements , name='elements'),
    path('index/' , views.index , name='index'),
]
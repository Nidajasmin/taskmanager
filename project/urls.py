from django.urls import path
from .views import *


urlpatterns=[
    path('pdash',projectdashboardview.as_view(),name='pdash'),
    path('padd',Addprojectview.as_view(),name='padd')
]
from django.urls import path 
from .views import *

app_name = 'blogsite_by_django'

urlpatterns = [
    path('', TopView.as_view(), name='top')
]
from django.urls import path  
from .views import *

app_name = 'keras_mnist'
# /keras_mnist/

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('upload/', upload, name='upload'),
]
from django.urls import path 
from .views import *

app_name = 'line_chatbot'
# /line_chatbot/

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('callback/', callback, name='callback'),  # LINEからのWebhookコールバック

]
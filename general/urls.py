from django.urls import path 
from .views import *

app_name = 'general'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),  # 各アプリの概要説明ページ
]
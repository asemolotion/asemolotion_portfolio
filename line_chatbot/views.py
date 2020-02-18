from django.shortcuts import render
from django.views.generic import TemplateView

class TopView(TemplateView):
    """ メイン画面表示　"""
    template_name = 'line_chatbot/top.html'


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

from .utils import parse_line_webhook, reply

class TopView(TemplateView):
    """ メイン画面表示　"""
    template_name = 'line_chatbot/top.html'


# LINEからのWebhookでのPOSTリクエストはCSRFトークンつけれないのでCSRFトークンを無視する。
@csrf_exempt
def callback(request):

    if request.method == 'POST':
        parse_line_webhook(request)


    return HttpResponse(200)
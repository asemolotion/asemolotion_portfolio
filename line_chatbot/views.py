from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

from .utils import parse_line_webhook, reply

class TopView(TemplateView):
    """ メイン画面表示　"""
    template_name = 'line_chatbot/top.html'


# LINEからのWebhookでのPOSTリクエストはCSRFトークンつけれないので。
@csrf_exempt
def callback(request):

    if request.method == 'POST':
        reply_token, text = parse_line_webhook(request)

        print(reply_token)
        print(text)

        reply(reply_token, text)


    return HttpResponse(200)
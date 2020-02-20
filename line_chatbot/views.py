from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

from .utils import parse_line_webhook, reply, message_reply


class TopView(TemplateView):
    """ メイン画面表示　"""
    template_name = 'line_chatbot/top.html'


def post_message(request):
    """ 
    メイン画面のフォームでLINEメッセージを試すことができるPOSTリクエストがくるView
    """
    message = request.POST.get('message')
    if message:
        reply_message = message_reply(message)
    else:
        # 空欄できたら一般的な答えを返す。
        default_message = 'リスト'
        reply_message = message_reply(default_message)

    context = {
        'message': message,
        'auto_reply': reply_message
    }

    return render(request, 'line_chatbot/top.html', context)


# LINEからのWebhookでのPOSTリクエストはCSRFトークンつけれないのでCSRFトークンを無視する。
@csrf_exempt
def callback(request):

    if request.method == 'POST':
        parse_line_webhook(request)


    return HttpResponse(200)
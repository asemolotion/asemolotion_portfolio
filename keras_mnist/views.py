from django.shortcuts import render
from django.views.generic import TemplateView

from PIL import Image 
import numpy as np
import base64
import tensorflow as tf 

import os
from django.conf import settings

#学習モデルのロード
from keras.models import load_model
model = load_model(os.path.join(settings.BASE_DIR, 'keras_mnist/models/mnist_simple.h5'))
graph = tf.get_default_graph()


class TopView(TemplateView):
    """ メイン画面表示　"""
    template_name = 'keras_mnist/top.html'


def mnist(img):
    """ 
    モデルを使って画像を判定した結果を返す関数
    
    Params: img: ndarray
    Returns: int: 0から9までのリストの順番
    """
    global graph
    with graph.as_default():
        result = model.predict(img,  batch_size=None, verbose=0, steps=None).argmax()

    return result

def upload(request):
    """
    フォームから画像ファイルをPOSTした時のビュー
    """
    _file = request.FILES.get('file')
    # ファイルを選択せずに送信すると、_file は Noneになる
    context = {}

    if request.method == "POST" and (_file is not None):
        img = Image.open(_file)

        gray_img = img.convert('L')
        img = gray_img.resize((28,28))
        img = np.array(img).reshape(1,784)
        
        label = mnist(img)

        # from keras.models import load_model
        # model_path = os.path.join(settings.BASE_DIR, 'keras_mnist/models', 'mnist_simple.h5')
        # model = load_model(model_path)
        # result = model.predict(img,  batch_size=None, verbose=0, steps=None)    
        # label = result

        _file.seek(0)
        file_name = _file
        src = base64.b64encode(_file.read()).decode()
        # src = str(src)[2:-1]

        context['result'] = (src, label)

    return render(request, 'keras_mnist/top.html', context)
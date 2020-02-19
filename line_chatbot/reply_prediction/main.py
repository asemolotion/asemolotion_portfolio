import os
from line_chatbot.reply_prediction.tokenizer import WordDivider
from line_chatbot.reply_prediction.vectorizer import Vectorizer
from line_chatbot.reply_prediction.distance_measure import DistanceMeasure


def predict_reply(user_message):
    """
    ユーザからのメッセージを受けて、話題に近いものを選択項目から予想して返す関数。

    Params:
        user_message: string: メッセージ
    Returns:
        nearest_option: string: 選択肢のタイトル
    """
    CUSTOM_DICT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'janome_custom_dict.csv')
    wd = WordDivider(CUSTOM_DICT_PATH, udic_type='simpledic', udic_enc='utf8')

    vectorizer = Vectorizer()
    measure = DistanceMeasure()

    word_list = wd.tokenize(message)
    mean_vec = vectorizer.get_mean_vectorized(word_list)
    nearest_options = measure.get_option_data(mean_vec)

    return nearest_options[0]

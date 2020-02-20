import os
from line_chatbot.reply_prediction.tokenizer import WordDivider
from line_chatbot.reply_prediction.vectorizer import Vectorizer
from line_chatbot.reply_prediction.distance_measure import DistanceMeasure

from line_chatbot.reply_prediction.setup_option_mapping import OPTIONS_DATA  # keywordsをとるため

def predict_reply(user_message):
    """
    ユーザからのメッセージを受けて、話題に近いものを選択項目から予想して返す関数。

    Params:
        user_message: string: メッセージ
    Returns:
        nearest_option: string: 選択肢のタイトル
    """
    CUSTOM_DICT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'janome_custom_dict.csv')
    # janomeのカスタム辞書csvを読み込んでインスタンスにする。
    wd = WordDivider(CUSTOM_DICT_PATH, udic_type='simpledic', udic_enc='utf8')

    vectorizer = Vectorizer()
    measure = DistanceMeasure()

    word_list = wd.tokenize(user_message)

    # word_listの中に、各オプションのkeywordsと同じ単語が入っていたらそのoptionで確定する
    word_set = set(word_list)

    for option in OPTIONS_DATA:
        keywords_set = set(option['keywords'])

        if word_set & keywords_set:  # 重複があった時

            return option['title']

    # 重複する単語がない時、ベクトルに変換してもっとも近い内容のものを返す。
    mean_vec = vectorizer.get_mean_vectorized(word_list)
    nearest_options = measure.get_option_data(mean_vec)
    

    return nearest_options[0]

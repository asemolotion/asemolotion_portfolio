import os
import pickle

from tokenizer import WordDivider
from vectorizer import Vectorizer


OPTIONS_DATA = [
    {
        'id': 0,
        'title': '急な病気やけがのとき',
    },
    {
        'id': 1,
        'title': 'イベント情報',
    },
    {
        'id': 2,
        'title': 'よくある質問、相談窓口',
        'subtext': """
        """
    },        
    {
        'id': 3,
        'title': '受け取る情報の設定',
        'subtext': """

        """
    },
    {
        'id': 4,
        'title': '道路公園等通報',
    },
    {
        'id': 5,
        'title': '防災・災害情報',
    },
    {
        'id': 6,
        'title': '家庭ごみの出し方ルール',
        'subtext': """
            ごみ
            燃えるごみ
            燃えないごみ
            資源ごみ
        """
    },
    {
        'id': 7,
        'title': '粗大ごみ受付',
        'subtext': """
            ごみ
            粗大ごみ収集の申し込み
            申し込み完了後の流れ
            粗大ごみ受付センター
            LINEからできない申し込み
            個人情報の取り扱い
            よくある質問        
        """
    },
    {
        'id': 8,
        'title': '引っ越し・証明案内',
        'subtext': """
            転入・転出に必要なものを知る
            引っ越し・証明よくあるQ&A

            住民票
            戸籍
            印鑑証明
            国民健康保険
            本人確認書類
            委任状
            ごみの出し方
            開庁時間・混雑状況
            区役所以外の証明取得         
        """
    },                      
]

CUSTOM_DICT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'janome_custom_dict.csv')
wd = WordDivider(CUSTOM_DICT_PATH, udic_type='simpledic', udic_enc='utf8')
vectorizer = Vectorizer()


options = []

for option in OPTIONS_DATA:
    text = option['title'] + option.get('subtext', '')
    word_list = wd.tokenize(text)

    unique_words = set(word_list)

    option['word_list'] = list(unique_words)  # 分割した単語を入れる。重複単語を消すとかはまたあとで。

    mean_vec = vectorizer.get_mean_vectorized(word_list)
    option['vec'] = mean_vec
    options.append(option)

PARENT_PATH = os.path.abspath(os.path.dirname(__file__))

pkl_file_path = os.path.join(PARENT_PATH, 'options.pkl')

with open(pkl_file_path, 'wb') as f:
    pickle.dump(options, f)
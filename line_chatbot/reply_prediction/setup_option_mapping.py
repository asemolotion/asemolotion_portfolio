import os
import pickle

from line_chatbot.reply_prediction.tokenizer import WordDivider
from line_chatbot.reply_prediction.vectorizer import Vectorizer


OPTIONS_DATA = [
    {
        'id': 0,
        'title': '急な病気やけがのとき',
        'keywords': ['病気', '怪我'],  # データごとに重要な単語。特別に重み付けるため。
        'word_list': [],
        'vec': None,
    },
    {
        'id': 1,
        'title': 'イベント情報',
        'keywords': ['イベント'],
        'word_list': [],
        'vec': None,        
    },
    {
        'id': 2,
        'title': 'よくある質問、相談窓口',
        'keywords': ['相談', '相談窓口'],
        'word_list': [],
        'vec': None,    
    },        
    {
        'id': 3,
        'title': '受け取る情報の設定',
        'keywords': ['LINEの設定', '設定'],
        'subtext': """

        """,
        'word_list': [],
        'vec': None,        
    },
    {
        'id': 4,
        'title': '道路公園等通報',
        'keywords': ['道路', '公園', '修理', '補修', '工事'],
        'word_list': [],
        'vec': None,        
    },
    {
        'id': 5,
        'title': '防災・災害情報',
        'keywords': ['災害', '避難', '緊急'],
        'word_list': [],
        'vec': None,        
    },
    {
        'id': 6,
        'title': '家庭ごみの出し方ルール',
        'keywords': ['ごみ', 'ゴミ', '家庭ごみ', '家庭ゴミ', '萌えるごみ', '燃えるゴミ', '燃えないゴミ', '燃えないごみ', '資源ごみ', '資源ゴミ'],
        'subtext': """
            ごみ
            燃えるごみ
            燃えないごみ
            資源ごみ
        """,
        'word_list': [],
        'vec': None,        
    },
    {
        'id': 7,
        'title': '粗大ごみ受付',
        'keywords': ['粗大ごみ', '粗大ゴミ'],        
        'subtext': """
            粗大ごみ収集の申し込み
            申し込み完了後の流れ
            粗大ごみ受付センター
            LINEからできない申し込み
            個人情報の取り扱い
            よくある質問        
        """,
        'word_list': [],
        'vec': None,        
    },
    {
        'id': 8,
        'title': '引っ越し・証明案内',
        'keywords': ['手続き', '引っ越し', '転入', '転出'],
        'subtext': """
            転入・転出に必要なものを知る
            引っ越し・証明よくあるQ&A

            住民票
            戸籍
            印鑑証明
            国民健康保険
            本人確認書類
            委任状
            開庁時間・混雑状況
            区役所以外の証明取得         
        """,
        'word_list': [],
        'vec': None,        
        # ごみの出し方を8から抜いた。
    },                      
]

CUSTOM_DICT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'janome_custom_dict.csv')

# インスタンスの準備
wd = WordDivider(CUSTOM_DICT_PATH, udic_type='simpledic', udic_enc='utf8')  # 文章->単語リストに分割
vectorizer = Vectorizer()  # 単語リスト->ベクトル


options = []

for option in OPTIONS_DATA:
    text = option['title'] + option.get('subtext', '')
    word_list = wd.tokenize(text)

    unique_words = set(word_list)
    option['word_list'] = list(unique_words)  # 分割した単語を入れる。重複単語を消すとかはまたあとで。
    
    # optionごとに重みをつけるために重複でも入れる単語を増やす。
    option['word_list'] += option['keywords']

    print(option['word_list'])
    mean_vec = vectorizer.get_mean_vectorized(option['word_list'])  # 各項目を表す単語リストの分散表現の平均をとる
    option['vec'] = mean_vec
    options.append(option)


# pickle 形式でoptionsというリストを保存。

PARENT_PATH = os.path.abspath(os.path.dirname(__file__))
pkl_file_path = os.path.join(PARENT_PATH, 'options.pkl')

with open(pkl_file_path, 'wb') as f:
    pickle.dump(options, f)
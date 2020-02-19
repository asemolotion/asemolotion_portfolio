import os
from fasttext import load_model
import numpy as np 

class Vectorizer:
    """
    文字列のリストを1つの平均ベクトルに変換するメソッドをもつクラス
    fasttextのモデルを使う。
    """    

    MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lid.176.ftz')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = load_model(self.MODEL_PATH)


    def vectorize(self, word):
        """
        文字列をベクトルに変換するメソッド

        Params:
            word: string: 形態素解析された単語
        Returns:
            vector: ndarray: 1次元のベクトル or None
        """
        try:
            vec = self.model[word]  # モデルにない単語ならNoneを返す
            return vec
        except:
            return None


    def get_mean_vectorized(self, word_list):
        """
        単語リストのベクトルの平均ベクトルを作って返すメソッド

        Params:
            word_list: list of string: 単語のリスト
        Returns:
            vec_list: list of ndarray: ベクトルのリスト
        """
        vec_list = []

        for word in word_list:
            vec = self.vectorize(word)
            
            # vec == None ならパス
            if vec.any():  
            # if vecだけだと "The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()"エラーになる。
            # ベクトルなので、どれかがNoneになるかで条件分岐が起こるので。
                vec_list.append(vec)
        
        mean_vector = self.mean_vectorized(vec_list)
        
        return mean_vector

    def mean_vectorized(self, vec_list):
        """
        複数のベクトルの平均ベクトルを作るメソッド
        
        Params:
            vec_list: list of vec: 単語ベクトルのリスト
        Returns:
            mean_vector: ndarray: 平均のベクトル
        """

        vec_tuple = tuple(vec_list)

        vec_stack = np.vstack(vec_tuple)
        vec_sum = np.sum(vec_stack, axis=0)
        vec_mean = vec_sum / 2

        return vec_mean



if __name__ == "__main__":
    words = ['hoge', 'piyo', 'puyo']

    vectorizer = Vectorizer()

    word_vec = vectorizer.get_mean_vectorized(words)

    print(word_vec)
    

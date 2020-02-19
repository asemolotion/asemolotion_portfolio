import os
import pickle
from scipy import spatial

class DistanceMeasure:
    """
    ユーザからのメッセージのベクトルと、
    全ての選択項目とのベクトルの距離を調べて、
    もっとも類似度の高い話題を返す処理をするクラス。
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SELF_LOCATION = os.path.abspath(os.path.dirname(__file__))
        self.load_options()

    def load_options(self):
        """
        コンストラクタで比較対象のベクトルを読み込む。
        """
        pkl_file = os.path.join(self.SELF_LOCATION, 'options.pkl')
        
        with open(pkl_file, 'rb') as f:
            self.options = pickle.load(f)


    def get_nearest_options(self, vec, count=5):
        """

        Params:
            vec: ndarray: １次元ベクトル
            count: int: 上位から取り出す個数。デフォルトは1個。
        Returns:
            nearest: リストのインデックス
        """
        sim_list = []

        for option in self.options:
            similarity = 1 - spatial.distance.cosine(vec, option['vec'])
            option['sim'] = similarity
            sim_list.append(similarity)
        
        nearest_indices = []
        
        for i in range(0, count):

            index = sim_list.index(max(sim_list))
            # sim_list.pop(index)  # 値を取り出す。-> だめ。
            sim_list[index] = 0  # 値を取り出すとindexが再度振られるので値を0にして続ける。

            nearest_indices.append(index)  # インデックスを足していく

        return nearest_indices

    def get_option_data(self, vec):
        """ 
        選択肢のうち、index番目のデータを取り出して返す関数

        Params:
            vec: ndarray: １次元ベクトル
        Returns:
            title list: list of string: self.optionsのindex番目のデータのリスト。
        """
        
        indices = self.get_nearest_options(vec)

        return [ self.options[index]['title'] for index in indices ]


if __name__ == "__main__":
    vec = [
        -0.875041, -2.5620067, -0.08499782, 0.01003265, -0.25335294, -1.1546848,
        -1.125962, 0.8443974, -0.99345684, -2.0430725, -0.71704334, 0.47081167,
        -0.38349903, -0.6362461, 0.11447591, -0.5288693]
    
    measure = DistanceMeasure()
    nearest = measure.get_option_data(vec)

    print(nearest)

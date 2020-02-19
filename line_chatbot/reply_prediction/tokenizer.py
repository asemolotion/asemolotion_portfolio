"""
githubの
asemolotion/lr-articles-lrtic-nb-app/blob/master/naivebayes/tokenizer.py　からコピー。

"""

from janome.tokenizer import Tokenizer

class WordDivider:
	"""
	日本語の文章をjanomeのトークナイザーを使って分割するクラス
	"""
	TARGET_CATEGORIES = [
		"カスタム名詞", 
		"名詞", 
		"動詞", 
		"形容詞", 
		"副詞", 
		"連体詞", 
		"感動詞",
	]

	def __init__(self, dictionary=None, **kwargs):
		"""
		コンパイルされたユーザカスタム辞書を読みこむ
		"""
		self.dictionary = dictionary
		self.tknz = Tokenizer(self.dictionary, **kwargs)

	def tokenize(self, text):
		"""
		textを形態素解析して、TARGET_CATEGORIESのものなら単語を返す

		Parameters:
			text: string
		Returns:
			word_list: list of tokenized word
		"""
		token_list = self.tknz.tokenize(text)
		word_list = []

		for token in token_list:

			if token.part_of_speech.split(',')[0] in self.TARGET_CATEGORIES:
				word_list.append(token.base_form)

		return word_list

	def get_words(self, contents):
		"""
		複数の記事をトークン化する関数

		Parameters:
			contents: list of string :
		Returns:
			tokenized_list: list of list of tokenized word : [['hoge','fuga'], [], [], ...]
		"""
		tokenized_list = []
		for content in contents:
			tokenized_list.append(self.tokenize(content))
		return tokenized_list

if __name__ == '__main__':
	wd = WordDivider()
	print(wd.tokenize('スターバックスのホゲホゲマルのコーヒーが冷たかったり温かったりします'))
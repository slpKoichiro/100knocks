import MeCab
import re
from collections import OrderedDict


class Morpheme(object):
    def __init__(self, mecab_file_name=None, source_file_name=None):
        self._mecab_file_name = mecab_file_name
        self._source_file_name = source_file_name

    @property
    def mecab_file_name(self):
        return self._mecab_file_name

    @mecab_file_name.setter
    def mecab_file_name(self, mecab_file_name):
        self._mecab_file_name = mecab_file_name

    @property
    def source_file_name(self):
        return self._source_file_name

    @source_file_name.setter
    def source_file_name(self, source_file_name):
        self._source_file_name = source_file_name

    """ 文字列解析の関数 """

    @classmethod
    def sentence_analysis(cls, sentence):
        tagger = MeCab.Tagger()  # 文字列(解析結果)のリスト
        """
        "表層形\t品詞, 品詞細分類1, 品詞細分類2, 品詞細分類3, 活用形, 活用型, 原形, 読み, 発音"
            という'文字列'のリストを
         [表層形, 品詞, ..., 発音]という'リスト'のリストに変換

        """
        # リスト(解析結果)のリスト
        morph_list = \
            [re.split('[,\t]', t) for t in tagger.parse(sentence).split('\n')]
        morph_list.pop(-1)  # EOSのデータを捨てる
        morph_list.pop(-1)  # 空白のデータを捨てる

        morph_dict_list = []
        for morph in morph_list:
            morph_dict = cls.reg_to_dict(morph)
            morph_dict_list.append(morph_dict)
        return morph_dict_list

    """ファイル名からファイルを読み込んで, そのテキストを解析する関数"""

    def file_analysis(self):
        with open(self.source_file_name, 'r', encoding='utf-8') as source_file:
            morph_dict_list = []
            for line in source_file:
                added_dict = self.sentence_analysis(line.rstrip())
                temp = self.sentence_analysis(line)
                if temp:  # 戻り値が空でない場合のみリストに追加する
                    morph_dict_list.extend(added_dict)
        return morph_dict_list

    """ 解析結果のファイルを読み込む関数 """

    def read_mecab_file(self):
        with open(self.mecab_file_name, 'r', encoding='utf-8') as mecab_file:
            morph_dict_list = []
            for morph_line in mecab_file:
                morph = re.split('[,\t]', morph_line.rstrip())
                if morph[0] == 'EOS':  # EOSは処理しない
                    continue
                morph_dict = self.reg_to_dict(morph)
                morph_dict_list.append(morph_dict)
        return morph_dict_list

    """ 解析結果を処理するための補助関数 """

    @classmethod
    def reg_to_dict(cls, morph):
        morph_dict = OrderedDict()
        morph_dict['surface'] = morph[0]  # 0: surface
        morph_dict['base'] = morph[7]  # 6: 基本形
        morph_dict['pos'] = morph[1]  # 1: 品詞
        morph_dict['pos1'] = morph[2]  # 2: 品詞細分類1
        return morph_dict


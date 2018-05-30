"""
1文節: Chunk
    形態素のリスト: morphs
    文節番号     : chunk_index
    係り先文節番号: dst (destination)
    係り元文節番号のリスト: srcs(sourceの複数形)
"""


class Chunk(object):
    """
    文節を表すクラス
    """

    def __init__(self, morphs, chunk_index, dst, srcs=None):
        """
        コンストラクタ
        :param morphs:
        :param chunk_index
        :param dst:
        :param srcs:
        """

        self.morphs = morphs  # 形態素のリスト
        self.chunk_index = chunk_index  # 文節インデックス
        self.dst = dst  # 係り先文節インデックス番号

        if srcs is None:
            self.srcs = []
        else:
            self.srcs = srcs  # 係り元文節インデックス番号のリスト

    def surface(self, remove_sign=False):
        """
        文節の表層形を返す
        :param remove_sign: 句読点などの記号を削除するか否か
        :return: 文節の表層形
        """
        if remove_sign is False:  # 句読点を含める
            return ''.join([morph.surface for morph in self.morphs])
        else:  # 句読点を含めない
            return ''.join([morph.surface for morph in self.morphs if morph.pos != '記号'])

    def output(self):
        print('文節番号:{0} \t文字列:{1} \t係り元:{2} \t係り先:{3}'
              .format(self.chunk_index,
                      self.surface(),
                      self.srcs,
                      self.dst))

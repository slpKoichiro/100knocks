"""
1文章: Syntax
    文節のリスト: Chunks
            形態素のリスト: morphs
            文節番号     : chunk_index
            係り先文節番号: dst(destination)
            係り元文節番号のリスト: srcs(sourceの複数形)
"""


class Syntax(object):
    """
    1文を表すクラス
    """

    def __init__(self, chunks):
        self.chunks = chunks  # 文節(Chunkオブジェクト)のリスト

        if self.chunks:
            # 各文節の係り元を求める
            for chunk in self.chunks:
                # int型じゃなくて、string型になってるので注意
                if chunk.dst != '-1':  # 係り先が'-1'は係り先なしを表すので注意
                    # 係り先(chunks[chunk.dst])の係り元文節番号リスト(srcs)に自分の文節番号を登録
                    self.chunks[int(chunk.dst)].srcs.append(chunk.chunk_index)

    def surface(self, remove_sign=False):
        """
        1文の中の表層形を求める
        :param remove_sign: 句読点などの記号を含めるか否か
        :return: 1文の中の表層形
        """
        return ''.join([chunk.surface(remove_sign) for chunk in self.chunks])

    def output(self):
        for chunk in self.chunks:
            chunk.output()

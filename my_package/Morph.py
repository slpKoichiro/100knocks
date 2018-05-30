class Morph(object):
    """
    形態素を表すクラス
    """

    def __init__(self, surface=None, base=None, pos=None, pos1=None):
        self.surface = surface  # 表層形
        self.base = base  # 基本形
        self.pos = pos  # 品詞
        self.pos1 = pos1  # 品詞細分類1

    # インスタンス変数の出力
    def output(self):
        print('表層形: {0}'.format(self.surface))
        print('基本形: {0}'.format(self.base))
        print('品詞: {0}'.format(self.pos))
        print('品詞細分類1: {0}'.format(self.pos1), end='\n' * 2)

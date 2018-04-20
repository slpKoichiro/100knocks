import random


class Typoglycemia(object):
    def __init__(self, sample):
        self._sample = sample

    @property
    def sample(self):
        return self._sample

    @sample.setter
    def sample(self, sample):
        self._sample = sample

    def randomize(self):
        words = self.sample.split(' ')  # include ';' and '.' ...
        print(words)  # debug
        random_words = words[:]  # リストのコピーは代入では無理. 代入は参照渡しになってしまう.
        target_index = []  # 並び替えるインデックスのリスト

        # 並び替えるインデックスの導出
        for i, w in enumerate(words):
            if len(w) > 4:
                target_index.append(i)

        random_index = target_index[:]  # リストのコピーは代入では無理. スライス or copyモジュールを使う
        random.shuffle(random_index)  # リストをシャッフル

        # 実際に並び替える
        for old, new in zip(target_index, random_index):
            random_words[old] = words[new]

        print(random_words)


if __name__ == '__main__':
    typo = Typoglycemia("I couldn't believe that I could actually understand what I was reading : "
                        "the phenomenal power of the human mind .")
    typo.randomize()

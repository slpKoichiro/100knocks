"""
51. 単語の切り出し
"""
import re
from my_package.sentence_split import sentence_split


def word_split(sentence):
    """
    1文を受け取って、単語を切り出す.
    記号(.,;:!?)は取り除いて単語部分のみ選択.
    フィラーのようなものも単語として扱う.
    :param sentence: １文
    :return: 単語のリスト
    """
    space_pattern = re.compile(r'\s')
    return [w.rstrip('.,;:?!') for w in space_pattern.split(sentence)]


def main():
    file_path = 'materials/nlp.txt'
    sentences = sentence_split(file_path)
    for sentence in sentences:
        words = word_split(sentence)
        for word in words:
            print(word)
        print('\n', end='')


if __name__ == '__main__':
    main()

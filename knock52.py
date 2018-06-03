"""
52. ステミング

参考サイト: https://hayataka2049.hatenablog.jp/entry/2018/03/25/203836#Porter%E3%82%92%E4%BD%BF%E3%81%86

"""
from my_package.sentence_split import sentence_split
from my_package.word_split import word_split
from nltk.stem.porter import PorterStemmer


def main():
    file_path = 'materials/nlp.txt'
    sentences = sentence_split(file_path)
    ps = PorterStemmer()  # 52
    for sentence in sentences:
        words = word_split(sentence)
        for word in words:
            stem = ps.stem(word)  # 52
            print('{0}\t{1}'.format(word, stem))
        print('\n', end='')


if __name__ == '__main__':
    main()

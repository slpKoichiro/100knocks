from Morpheme import Morpheme
from collections import defaultdict

def main():
    file_name = 'materials/neko.txt.mecab'
    morph = Morpheme(mecab_file_name=file_name)
    result = morph.read_mecab_file()  # 辞書のリスト

    count_dict = defaultdict(int)  # key: 単語(1列目), value: 単語の出現回数
    for d in result:
        count_dict[d['surface']] += 1

    # ソートして出力
    for word, count in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
        print('{1}\t{0}'.format(word, count))


if __name__ == '__main__':
    main()

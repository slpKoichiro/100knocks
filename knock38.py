from Morpheme import Morpheme
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def main():
    file_name = 'materials/neko.txt.mecab'
    morph = Morpheme(mecab_file_name=file_name)
    result = morph.read_mecab_file()  # 辞書のリスト

    count_dict = defaultdict(int)  # key: 単語(1列目), value: 単語の出現回数
    for d in result:
        count_dict[d['surface']] += 1

    #  日本語フォントを使用可能に
    fp = FontProperties(fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')

    # ヒストグラムのデータ指定
    # histがリストを渡せば頑張って出現頻度ごとに分類してくれる
    plt.hist(
        count_dict.values(),  # データのリスト(単語の出現回数のリスト)
        bins=20,  # ビンの数
        range=(1, 20))  # 値の範囲

    # x軸の値の範囲の調整
    plt.xlim(xmin=1, xmax=20)

    # グラフのタイトル、ラベル指定
    plt.title("38. ヒストグラム", fontproperties=fp)
    plt.xlabel('出現頻度', fontproperties=fp)
    plt.ylabel('単語の種類数', fontproperties=fp)

    # グリッドを表示
    plt.grid(axis='y')

    # 表示
    plt.show()


if __name__ == '__main__':
    main()

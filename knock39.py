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

    count = sorted(count_dict.values(), reverse=True)  # 単語の出現頻度 (回数) 多いもの順

    #  日本語フォントを使用可能に
    fp = FontProperties(fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')

    # 散布図のデータ指定
    # x, y には配列(リスト)をそれぞれ渡す
    # 出現回数(x)を順位(y)付けした組を座標とする(イメージはzipに近い)
    plt.scatter(
        range(1, len(count)+1),  # x軸：順位(1位〜単語の個数までの順位がある)
        count  # y軸：出現頻度（回数）
    )

    # 軸の値の範囲の調整
    plt.xlim(1, len(count) + 1)
    plt.ylim(1, count[0])  # count[0] = 最大の出現回数

    # 対数グラフに
    plt.xscale('log')
    plt.yscale('log')

    # グラフのタイトル、ラベル指定
    plt.title("39. Zipfの法則", fontproperties=fp)
    plt.xlabel('出現度順位', fontproperties=fp)
    plt.ylabel('出現頻度', fontproperties=fp)

    # グリッドを表示
    plt.grid(axis='both')

    # 表示
    plt.show()


if __name__ == '__main__':
    main()

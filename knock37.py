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

    # ソートして上位10個を取り出す
    top10_word = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    label = [x[0] for x in top10_word]  # 単語(名), 横軸のラベル
    height = [x[1] for x in top10_word]  # 単語の出現回数, 縦軸

    #  日本語フォントを使用可能に
    fp = FontProperties(fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')

    # 棒グラフのデータ指定
    plt.bar(range(10), height, align="center")  # xの値, yの値, 棒グラフの表示位置

    # x軸のラベルの指定
    plt.xticks(
        range(0, 10),  # x軸の値（0,1,2...9）
        label,  # それに対応するラベル
        fontproperties=fp  # 使うフォント情報
    )

    # x軸の値の範囲の調整
    plt.xlim(
        xmin=-1, xmax=10  # -1〜10（左右に1の余裕を持たせて見栄え良く）
    )

    # グラフのタイトル、ラベル指定
    plt.title(
        '37. 頻度上位10語',  # タイトル
        fontproperties=fp  # 使うフォント情報
    )
    plt.xlabel(
        '出現頻度が高い10語',  # x軸ラベル
        fontproperties=fp  # 使うフォント情報
    )
    plt.ylabel(
        '出現頻度',  # y軸ラベル
        fontproperties=fp  # 使うフォント情報
    )

    # グリッドを表示
    plt.grid(axis='y')

    # 表示
    plt.show()


if __name__ == '__main__':
    main()

"""
neko.txt.cabocha の説明

1行目

    *
    文節番号
    係り先の文節番号(係り先なし:-1)
    主辞の形態素番号/機能語の形態素番号
    係り関係のスコア(大きい方が係りやすい)

2行目

    表層形 （Tab区切り）
    品詞
    品詞細分類1
    品詞細分類2
    品詞細分類3
    活用形
    活用型
    原形
    読み
    発音

"""

import CaboCha


def exce_cabocha(input_file_name, output_file_name, dict_pass=None):
    """
    入力ファイル(文章ファイル)をCaboChaにかけて出力ファイルに結果を出力
    :param input_file_name: 入力テキストファイル
    :param output_file_name: CaboChaの出力先ファイル
    :param dict_pass: CaboChaの辞書のパス
    :return: なし
    """
    if dict_pass is None:  # 辞書指定なし
        c = CaboCha.Parser()
    else:  # 辞書指定あり
        c = CaboCha.Parser('-d ' + dict_pass)

    with open(input_file_name, mode='r', encoding='utf-8') as input_file, \
            open(output_file_name, mode='w', encoding='utf-8') as output_file:
        for line in input_file:
            parsered = c.parse(line.rstrip())
            output_file.write(parsered.toString(CaboCha.FORMAT_LATTICE))

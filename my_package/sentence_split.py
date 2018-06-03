import re


def sentence_split(file_path):
    """
    与えられたファイル名のファイルをオープンして、文区切りを行う.
    :param file_path: ファイル名
    :return: 文のリスト
    """
    # すべての文章は大文字から始まるとした.
    # はじめのグループがターゲット、後半は再帰的に処理(次のターゲット)
    sentences = []
    pattern = re.compile(r'([A-Z].*?[\.|;|:|\?|!])\s([A-Z].*)')
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            while True:
                match_result = pattern.match(line)
                if match_result:
                    sentences.append(match_result.group(1))  # ターゲットをリストへ
                    line = match_result.group(2)  # 後半は次回のターゲットへ
                else:  # マッチしなかった場合(空行 or 1文からなる行)
                    if line != '':  # 空行でなければ出力
                        sentences.append(line)
                    break
    return sentences

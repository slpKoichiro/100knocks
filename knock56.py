"""
56. 共参照解析

(例)
    <start>: sentence中の何個目の単語から始まっているか(1スタート)
    <end>:   「終わり+1」のインデックス番号
        -> [start:end-1]のidが一致する
    <head>: 核となる語のインデックス番号？

      <coreference>
        <mention representative="true">
          <sentence>22</sentence>
          <start>7</start>
          <end>11</end>
          <head>10</head>
          <text>many speech recognition systems</text>
        </mention>
        <mention>
          <sentence>25</sentence>
          <start>1</start>
          <end>3</end>
          <head>2</head>
          <text>These systems</text>
        </mention>
        <mention>
          <sentence>26</sentence>
          <start>35</start>
          <end>37</end>
          <head>36</head>
          <text>these systems</text>
        </mention>
        <mention>
          <sentence>47</sentence>
          <start>20</start>
          <end>22</end>
          <head>21</head>
          <text>the systems</text>
        </mention>
      </coreference>






<root>: root
    <document>: root[0]
        <docId>:       root[0][0]

        <sentences>:   root[0][1]
            <sentence>:     root[0][1][0]
                <tokens>:       root[0][1][0][0]

                    <token>:        root[0][1][0][0][0]
                        <word>:     root[0][1][0][0][0][0]
                        <lemma>:    root[0][1][0][0][0][1]
                        <CharacterOffsetBegin>
                        <CharacterOffsetEnd>
                        <POS>
                        <NER>
                        <Speaker>


                    .
                    .
                    .
                    <token>:

                <parse>:        root[0][1][0][1]
                <dependencies>: root[0][1][0][2]
                .
                .
                .
                <dependencies>
            <sentence>:     root[0][1][2]
            .
            .
            .
            <sentence>:

        <coreference>: root[0][2]
            <coreference>:  root[0][2][0]
                <mention>:      root[0][2][0][0]
                    <sentence>:     root[0][2][0][0][0]
                    <start>:        root[0][2][0][0][1]
                    <end>:          root[0][2][0][0][2]
                    <head>:         root[0][2][0][0][3]
                    <text>:         root[0][2][0][0][4]
                <mention>:      root[0][2][0][1]
                .
                .
                .
                <mention>
            <coreference>:  root[0][2][1]
            .
            .
            .
            <coreference>

"""

from xml.etree import ElementTree


class CorefMention(object):
    def __init__(self, sentence_id, start, end, representative=None):
        self.sentence_id = sentence_id
        self.start = start
        self.end = end - 1
        self.representative = representative
        self.scope = range(start, end + 1)


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()

    # 単語を拾っていく
    sentences = []  # [文章番号][単語番号]で単語にアクセスしたい
    for sentence in root[0][1]:
        words = []  # 1文中の単語のリスト
        tokens = sentence[0]
        for token in tokens:
            words.append(token[0].text)
        sentences.append(words)

    # coreferenceを集める
    coreferences = []
    for coreference in root[0][2]:
        temp_corefs_list = []
        representative = None
        for mention in coreference:  # 共参照中の要素を順に処理
            # 各情報をGET
            sentence_id = int(mention[0].text)
            start = int(mention[1].text)
            end = int(mention[2].text)
            text = mention[4].text
            # 代表参照のとき
            if mention.get('representative') == 'true':
                representative = text  # 参照される文字列をGET
            # 代表参照でないとき
            else:
                coref = CorefMention(sentence_id, start, end)  # 参照する側のインスタンスを作成
                temp_corefs_list.append(coref)  # 一時的なリストに追加
        # 参照先の文字列を設定
        for coref in temp_corefs_list:
            coref.representative = representative
        # リストをまとめる
        coreferences.extend(temp_corefs_list)

    # 代表参照を挿入しながら単語を出力していく
    insert_flag = False
    for sentence_id, sentence in enumerate(sentences, 1):
        # 文章番号が一致する非参照側の部分リストを作成
        specific_coreferences = [coref for coref in coreferences if coref.sentence_id == sentence_id]
        # 1文章中の単語を1つずつ処理
        for word_id, word in enumerate(sentence, 1):
            # その単語のidが非参照側のどれかの文字列の開始位置と一致するかをチェック
            for coref in specific_coreferences:
                # 代表参照の挿入
                if word_id == coref.start:
                    insert_sentence = '[' + coref.representative + ']'
                    print(insert_sentence, end=' ')
                    print('(', end='')
                    end = coref.end  # 終わりの ')' を挿入する位置を記憶
                    insert_flag = True
                    break
            # 単語を出力する
            if insert_flag is True and word_id == end:  # 最後の')'を含めて出力
                print(word + ')', end=' ')
                insert_flag = False
            else:  # 普通に単語を出力
                print(word, end=' ')

        print('')


if __name__ == '__main__':
    main()

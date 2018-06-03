"""
59. S式の解析

(例)
        <parse>(ROOT (S (PP (IN During) (NP (DT this) (NN time))) (, ,) (NP (JJ many) (NNS chatterbots)) (VP (VBD were) (VP (VBN written) (PP (VBG including) (NP (NNP PARRY) (, ,) (NNP Racter) (, ,) (CC and) (NNP Jabberwacky))))) (. .))) </parse>




<root>: root
    <document>: root[0]
        <docId>:       root[0][0]

        <sentences>:   root[0][1]
            <sentence>:     root[0][1][0]
                <tokens>:       root[0][1][0][0]

                    <token>:        root[0][1][0][0][0]
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
"""

from xml.etree import ElementTree
import re


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()
    sentences = root[0][1]
    sentence_list = []
    # '(', ')', tag, text すべてをひっくるめて1つのリストにする
    for sentence in sentences:
        parse = sentence[1]
        t1 = re.sub(r'\)', r' )', parse.text)
        t2 = re.sub(r'\(', r'( ', t1)
        split_text = t2.split(' ')
        sentence_list.append(split_text)

    for sentence in sentence_list:  # sentence: '(', ')', tag, textを要素とするリスト(1文を表現)
        for i, token in enumerate(sentence):  # token: '(', ')', tag, text
            # (NP text) をチェックする. textは入れ子
            if token == 'NP':
                check_list = sentence[i + 1:]  # '(' 'NP' '('  ... ')' における ( ... )がcheck_list
                left_sign = 1  # 左のカッコ'(' の数, NPの左のカッコにより初期値1
                right_sign = 0  # 右のカッコ')' の数
                text_flag = True  # 次に読み込む ')'でも'('でもない文字列はtagでなくtext -> True
                text = []  # textの集合
                for elem in check_list:
                    if elem == ')':  # 右カッコ
                        right_sign += 1
                        text_flag = False  # カッコ以外で次くる文字列はtag
                        if left_sign == right_sign:  # カッコの整合性が取れたら終わり!!
                            break
                    elif elem == '(':  # 左カッコ
                        left_sign += 1
                        text_flag = False  # カッコ以外で次くる文字列はtag
                    else:  # tag or text
                        if text_flag:  # textとして捉えたとき
                            text.append(elem)
                            text_flag = False  # カッコ以外で次くる文字列はtag
                        else:  # tagとして捉えた時
                            text_flag = True  # カッコ以外で次来る文字列はtext(tagの直後にしかtextは来ないので、trueになるのはここの分岐のみ)
                # 出力！！
                print(' '.join(text))


if __name__ == '__main__':
    main()

import os
import subprocess
import xml.etree.ElementTree as ET

fname_parsed = 'materials/nlp.txt.xml'
# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# sentence列挙、1文ずつ処理
for sentence in root.iterfind('./document/sentences/sentence'):
    sent_id = int(sentence.get('id'))  # sentenceのid

    # それぞれの語の辞書を作成
    dict_pred = {}  # {述語のidx, 述語のtext}
    dict_nsubj = {}  # {述語のidx, 述語とnsubj関係の子のtext（＝主語）}
    dict_dobj = {}  # {述語のidx, 述語とdobj関係の子のtext（＝目的語）}

    # dependencies列挙
    for dep in sentence.iterfind(
            './dependencies[@type="collapsed-dependencies"]/dep'
    ):

        # 関係チェック
        dep_type = dep.get('type')
        if dep_type == 'nsubj' or dep_type == 'dobj':

            # 述語の辞書に追加
            govr = dep.find('./governor')
            idx = govr.get('idx')
            dict_pred[idx] = govr.text  # 重複するが無害なのでチェックは省略

            # 主語or目的語の辞書に追加
            if dep_type == 'nsubj':
                dict_nsubj[idx] = dep.find('./dependent').text
            else:
                dict_dobj[idx] = dep.find('./dependent').text

    # 述語を列挙、主語と目的語の両方を持つもののみ出力
    for idx, pred in sorted(dict_pred.items(), key=lambda x: x[0]):
        nsubj = dict_nsubj.get(idx)
        dobj = dict_dobj.get(idx)
        if nsubj is not None and dobj is not None:
            print('{}\t{}\t{}'.format(nsubj, pred, dobj))

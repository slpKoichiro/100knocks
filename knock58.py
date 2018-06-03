"""
58. タプルの抽出

(例)
    (1) 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
        つまり, dep type == "nsubj" or "dobj" の governor が述語

          <dep type="nsubj">
            <governor idx="18">field</governor>
            <dependent idx="3">processing</dependent>
          </dep>

          <dep type="dobj">
            <governor idx="13">enabling</governor>
            <dependent idx="14">computers</dependent>
          </dep>

    (2) 主語: 述語からnsubj関係にある子（dependent）
        つまり, dep type == "nsubj" のときの dependant が主語

    (3) 目的語: 述語からdobj関係にある子（dependent）
        つまり, dep type == "dobj" のときの dependant が目的語

"""

from xml.etree import ElementTree


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()

    sentences = root[0][1]
    for sentence in sentences:
        predicate_subject = []  # ((述語id, 述語), (主語id, 主語)) のリスト
        predicate_object = []  # ((目的語id, 目的語), (目的語id, 目的語)) のリスト
        for dependencies in sentence.findall('dependencies'):  # 3種類dependenciesはあるらしいが
            if dependencies.get('type') == "collapsed-dependencies":  # 'collapsed-dependencies' の場合のみ処理
                for dep in dependencies:
                    if dep.get('type') == 'nsubj':  # 述語-主語
                        predicate_tuple = (dep[0].get('idx'), dep[0].text)  # 述語
                        subject_tuple = (dep[1].get('idx'), dep[1].text)  # 主語
                        predicate_subject.append((predicate_tuple, subject_tuple))  # タプルをリストに追加
                    elif dep.get('type') == 'dobj':  # 述語-目的語
                        predicate_tuple = (dep[0].get('idx'), dep[0].text)  # 述語
                        object_tuple = (dep[1].get('idx'), dep[1].text)  # 目的語
                        predicate_object.append((predicate_tuple, object_tuple))  # タプルをリストに追加

        # 今見てきたsentence(文)について, 主語, 述語, 目的語 が全部揃っていたら出力
        for pre_sub in predicate_subject:  # 述語-主語のリストを見ていく
            pre_id_of_sub = pre_sub[0][0]  # 述語-主語側の述語のid
            for pre_obj in predicate_object:  # 述語-目的語のリストを見ていく
                pre_id_of_obj = pre_obj[0][0]  # 述語-目的語側の述語のid
                if pre_id_of_sub == pre_id_of_obj:  # 2つの述語idが一致したら
                    sub = pre_sub[1][1]  # 主語
                    pre = pre_sub[0][1]  # 述語
                    obj = pre_obj[1][1]  # 目的語
                    print('{0}\t{1}\t{2}'.format(sub, pre, obj))


if __name__ == '__main__':
    main()

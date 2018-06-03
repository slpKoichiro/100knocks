"""
57. 係り受け解析

(例) 問題にされているのはこっち(collapsed-dependencies)
        <dependencies type="collapsed-dependencies">
          <dep type="root">
            <governor idx="0">ROOT</governor>
            <dependent idx="18">field</dependent>
          </dep>
          <dep type="amod">
            <governor idx="3">processing</governor>
            <dependent idx="1">Natural</dependent>
          </dep>

    basic-dependenciesは対象外
        <dependencies type="basic-dependencies">
          <dep type="root">
            <governor idx="0">ROOT</governor>
            <dependent idx="18">field</dependent>
          </dep>
          <dep type="amod">
            <governor idx="3">processing</governor>
            <dependent idx="1">Natural</dependent>
          </dep>







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
import pydot_ng as pydot


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()

    sentences = root[0][1]
    dot_list = []
    for sentence in sentences:
        dot_expression = []
        for dependencies in sentence.findall('dependencies'):  # 3種類dependenciesはあるらしいが
            if dependencies.get('type') == "collapsed-dependencies":  # 'collapsed-dependencies' の場合のみ処理
                for dep in dependencies:
                    if dep.get('type') != 'punct':  # 句読点絡みは無視
                        from_node = (dep[0].get('idx'), dep[0].text)  # 入力ノード
                        to_node = (dep[1].get('idx'), dep[1].text)  # 出力ノード
                        dot_expression.append((from_node, to_node))  # 辺をリストに追加
        dot_list.append(dot_expression)

    # knock44 と全く同じ
    # グラフ(DOTオブジェクト)の作成
    sentence_id = int(input('何文目のグラフを出力しますか？: '))
    graph = pydot.Dot(graph_type='digraph')  # 有向グラフを選択
    for edge in dot_list[sentence_id - 1]:  # edge: タプルのタプル((id1, label1), (id2, label2))
        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノード追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # エッジ追加
        graph.add_edge(pydot.Edge(id1, id2))
    # 画像出力
    png_file_pass = 'output_result/knock57/{0}.png'.format(sentence_id)
    graph.write_png(png_file_pass)


if __name__ == '__main__':
    main()

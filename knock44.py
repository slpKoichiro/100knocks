"""
42. 係り元と係り先の文節の表示

memo:はじめにOSに対して sudo apt install graphviz
     を行ってから, pydot_ngを入れる必要がある(pythonパッケージのgraphvizは不要？)
     先にOSにgraphvizを入れることで、write_png()などの関数が使えるようになる.
     ただし, pycharmにはそんな関数はないと思うけど？って怒られて怒りのマーカーでピカピカするし、
     補完も効かない. これは我慢しよう.

     先にOSにgraphvizを入れずに, pip install graphvizを行ってしまうと,
     競合の関係なのかわからないが、Dotオブジェクトのwrite_png(), write_pos()といった関数が使えない.
     (write()関数は使用可能. なにかのファイルのpathをいじればいけるらしい？難しそうで逃げた.)
"""

from my_package.read_cabocha_file import read_cabocha_file
import pydot_ng as pydot


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    dot_list = []  # 各文のDOT表現
    for syntax in syntax_structure:  # syntax: 1文
        dot_expression = []  # ある1文のDOT表現
        for chunk in syntax.chunks:  # chunk: 1文節
            dst_index = int(chunk.dst)  # 係り先の文節番号
            if dst_index != -1:  # 係り先が存在する場合のみ処理
                # 係り元のテキスト(記号削除ver)
                removed_sign_src_surface = chunk.surface(remove_sign=True)
                # 係り先のテキスト(記号削除ver)
                removed_sign_dst_surface = syntax.chunks[dst_index].surface(remove_sign=True)
                # 係り元、係り先ともに文字列として存在すれば辺としてdot_expressionに追加
                # 辺: ((係り元文節番号, 係り元の表層形), (係り先文節番号, 係り先の表層形)) // タプルのタプル
                if removed_sign_src_surface != '' and removed_sign_dst_surface != '':
                    dot_expression.append(((chunk.chunk_index, removed_sign_src_surface),
                                           (dst_index, removed_sign_dst_surface)))
        dot_list.append(dot_expression)  # 1文のDOT表現をリストに追加

    # グラフ(DOTオブジェクト)の作成
    syntax_id = int(input('何文目のグラフを出力しますか？: '))
    graph = pydot.Dot(graph_type='digraph')  # 有向グラフを選択
    # ひとつの文節のみからなる文の場合(係り受けなし)
    if len(dot_list[syntax_id - 1]) == 0:  # 1つのノードのみ出力
        graph.add_node((pydot.Node(1, label=syntax_structure[syntax_id - 1].surface(remove_sign=True))))
    else:  # 係り受けが存在する場合は有向グラフを作成
        for edge in dot_list[syntax_id - 1]:  # edge: タプルのタプル((id1, label1), (id2, label2))
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
    png_file_pass = 'output_result/knock44/{0}.png'.format(syntax_id)
    graph.write_png(png_file_pass)


if __name__ == '__main__':
    main()

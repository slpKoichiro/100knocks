"""
49. 名詞間の係り受けパスの抽出
"""

from my_package.read_cabocha_file import read_cabocha_file
from my_package.search_morph_in_chunk import search_morph_in_chunk


def extract_root_pass(chunk, syntax):
    """
    与えられた文節から根へのパスを文節番号のリストとして返す
    :param chunk: 文節
    :param syntax: 文節chunkが含まれる1文
    :return: 文節から根へのパス(文節番号のリスト)
    """
    chunk_indexs = [chunk.chunk_index]  # rootに至るまでのpassのノード
    dst = chunk.dst  # 係り先の文節番号
    # dstを順次rootまでたどって行く
    while dst != '-1':
        chunk = syntax.chunks[int(dst)]
        chunk_indexs.append(chunk.chunk_index)
        dst = chunk.dst
    return chunk_indexs


def extract_pass_between_two_chunks(chunk_x, chunk_y, syntax, separater=' -> '):
    # xの文節番号がyの文節番号よりも小さくなるようにする
    if chunk_x.chunk_index < chunk_y.chunk_index:
        pass
    else:
        chunk_x, chunk_y = chunk_y, chunk_x
    x_index = chunk_x.chunk_index
    y_index = chunk_y.chunk_index

    # 文節X, Y のrootへのpassをそれぞれ求める
    x_pass = extract_root_pass(chunk_x, syntax)
    y_pass = extract_root_pass(chunk_y, syntax)

    for x_node in x_pass:
        if x_node in y_pass:

            # 文節Xの名詞を'X'に置換したsurfaceの作成
            x_token = ''
            for morph in chunk_x.morphs:
                if morph.pos == '名詞':
                    x_token += 'X'
                elif morph.pos != '記号':
                    x_token += morph.surface

            # 文節Yの名詞を'Y'に置換したsurfaceの作成
            y_token = ''
            for morph in chunk_y.morphs:
                if morph.pos == '名詞':
                    y_token += 'Y'
                else:
                    y_token += morph.surface

            if x_node == y_index:  # 文節Xから構文木の根に至る経路上に文節Yが存在する場合
                # 文節Xから文節Yのパスを表示
                last = x_pass.index(y_index)
                shortest_pass = separater.join([syntax.chunks[int(t)].surface(remove_sign=True)
                                                for t in x_pass[1:last]])

                if shortest_pass != '':
                    shortest_pass = x_token + separater + shortest_pass + separater + y_token
                else:
                    shortest_pass = x_token + separater + y_token
            else:  # 文節Xと文節Yから構文木の根に至る経路上で共通の文節Kで交わる場合:
                # 文節Xから文節Kに至る直前のパスと文節Yから文節Kに至る直前までのパス，文節Kの内容を表示
                k_index = x_node
                # X - > K
                last_x = x_pass.index(k_index)  # 文節KはXのパスの中のどの位置で出てきたかを求める
                # 先頭のXと末尾のKを除いたパスを求める
                shortest_x_pass = separater.join([syntax.chunks[int(t)].surface(remove_sign=True)
                                                  for t in x_pass[1:last_x]])
                if shortest_x_pass != '':
                    shortest_x_pass = x_token + separater + shortest_x_pass
                else:
                    shortest_x_pass = x_token

                # Y -> K
                last_y = y_pass.index(k_index)  # 文節KはXのパスの中のどの位置で出てきたかを求める
                # 先頭のXと末尾のKを除いたパスを求める
                shortest_y_pass = separater.join([syntax.chunks[int(t)].surface(remove_sign=True)
                                                  for t in y_pass[1:last_y]])
                if shortest_y_pass != '':
                    shortest_y_pass = y_token + separater + shortest_y_pass
                else:
                    shortest_y_pass = y_token

                # X -> K | Y -> K | K
                shortest_pass = shortest_x_pass + ' | ' + shortest_y_pass + ' | ' + syntax.chunks[int(k_index)].surface(
                    remove_sign=True)
            break
    return shortest_pass


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    with open('output_result/knock49.txt', 'w', encoding='utf-8') as output_file:
        for syntax in syntax_structure:  # syntax: 1文
            noun_chunks = []  # ある1文(syntax)内における名詞句(名詞で終わる文節)のリスト
            # 1文内の名詞句を探しに行くループ
            for chunk in syntax.chunks:  # chunk: 1文節
                morphs_with_noun = search_morph_in_chunk(chunk, '名詞')
                if morphs_with_noun:  # 名詞が含まれている文節ならば
                    noun_chunks.append(chunk)  # 名詞句のリストに追加
            if len(noun_chunks) >= 2:  # 文節内に名詞句が2つ以上あった場合は
                # 名詞句の最短を求める
                for i, chunk_x in enumerate(noun_chunks):
                    for chunk_y in noun_chunks[i + 1:]:
                        shortest_pass = extract_pass_between_two_chunks(chunk_x, chunk_y, syntax)
                        print(shortest_pass, file=output_file)


if __name__ == '__main__':
    main()

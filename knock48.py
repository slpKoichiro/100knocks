"""
48. 名詞から根へのパスの抽出
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


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    with open('materials/knock48.txt', 'w', encoding='utf-8') as output_file:
        for syntax in syntax_structure:  # syntax: 1文
            for chunk in syntax.chunks:  # chunk: 1文節
                # 文節内に名詞があるか探す
                morphs_with_noun = search_morph_in_chunk(chunk, '名詞')
                if morphs_with_noun:  # 名詞が含まれている文節ならば
                    root_pass_of_index = extract_root_pass(chunk, syntax)  # 根へのpassを求める
                    root_pass = ' -> '.join([syntax.chunks[int(t)].surface(remove_sign=True)
                                             for t in root_pass_of_index])
                    print(root_pass, file=output_file)


if __name__ == '__main__':
    main()

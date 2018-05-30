"""
47. 機能動詞構文のマイニング
"""

from my_package.read_cabocha_file import read_cabocha_file
from my_package.search_morph_in_chunk import search_morph_in_chunk


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    find_verb_flag = False  # 動詞を発見したかどうかのフラグ
    for syntax in syntax_structure:  # syntax: 1文
        for chunk in syntax.chunks:  # chunk: 1文節
            find_sahen_flag = False  # "サ変接続名詞" + を("助詞") の文節が見つかったか否かのフラグ(knock47)
            t = search_morph_in_chunk(chunk, '動詞', 1)  # 文節内から動詞の形態素を1つ探す
            if t:  # 見つかった場合
                predicate_base = t[0].base  # 動詞の基本形を述語に
                find_verb_flag = True  # 動詞見つかりましたフラグON!!
            if find_verb_flag is True:  # 動詞を含む文節が見つかった場合は
                find_verb_flag = False
                postposition_list = []  # 助詞のリスト
                postposition_chunk_list = []  # 助詞を含む文節のリスト
                for src in chunk.srcs:  # 係り元の文節内に助詞があるか探す
                    src_chunk = syntax.chunks[int(src)]
                    last_morph = src_chunk.morphs[-1]  # 文節内の最後の形態素
                    if last_morph.pos == '助詞':  # 文節内の最後の形態素が助詞だったら
                        # (knock47で追加)
                        # さらに、その文節が "サ変接続名詞" + を("助詞") で構成される文節かをチェック
                        if len(src_chunk.morphs) == 2 and \
                                src_chunk.morphs[0].pos == '名詞' and \
                                src_chunk.morphs[0].pos1 == 'サ変接続' and \
                                src_chunk.morphs[1].pos == '助詞' and \
                                src_chunk.morphs[1].surface == 'を':
                            sahen_wo_chunk_surface = src_chunk.surface(remove_sign=True)
                            find_sahen_flag = True
                        else:
                            postposition_list.append(last_morph.surface)  # その表層形をリストに追加
                            # その助詞を含む文節をリストに追加(knock46で追加)
                            postposition_chunk = src_chunk.surface(remove_sign=True)
                            postposition_chunk_list.append(postposition_chunk)
                # "サ変接続名詞" + "助詞" の文節が見つかった場合のみ出力
                if find_sahen_flag is True:
                    print('{0}\t{1}\t{2}'
                          .format(sahen_wo_chunk_surface+predicate_base,
                                  ' '.join(postposition_list),
                                  ' '.join(postposition_chunk_list)))


if __name__ == '__main__':
    main()

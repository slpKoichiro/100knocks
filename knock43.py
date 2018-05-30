"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
"""

from my_package.read_cabocha_file import read_cabocha_file


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    for syntax in syntax_structure:  # syntax: 1文
        for chunk in syntax.chunks:  # chunk: 1文節
            dst_index = int(chunk.dst)
            if dst_index != -1:  # 係り先が存在する場合のみ処理
                # 係り元の文節内の品詞を集める
                src_pos_list = []
                for morph in chunk.morphs:
                    src_pos_list.append(morph.pos)
                # 係り先の文節内の品詞を集める
                dst_pos_list = []
                for morph in syntax.chunks[dst_index].morphs:
                    dst_pos_list.append(morph.pos)

                src_flag = '名詞' in src_pos_list
                dst_flag = '動詞' in dst_pos_list
                if src_flag is True and dst_flag is True:
                    # 係り元のテキスト(記号削除ver)
                    removed_sign_src_surface = chunk.surface(remove_sign=True)
                    # 係り先のテキスト(記号削除ver)
                    removed_sign_dst_surface = syntax.chunks[dst_index].surface(remove_sign=True)
                    # 係り元、係り先ともに文字列として存在すれば出力
                    if removed_sign_src_surface != '' and removed_sign_dst_surface != '':
                        print(removed_sign_src_surface + '\t' + removed_sign_dst_surface)


if __name__ == '__main__':
    main()

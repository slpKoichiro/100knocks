"""
42. 係り元と係り先の文節の表示
"""

from my_package.read_cabocha_file import read_cabocha_file


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    for syntax in syntax_structure:  # syntax: 1文
        for chunk in syntax.chunks:  # chunk: 1文節
            dst_index = int(chunk.dst)
            if dst_index != -1:  # 係り先が存在する場合のみ処理
                # 係り元のテキスト(記号削除ver)
                removed_sign_src_surface = chunk.surface(remove_sign=True)
                # 係り先のテキスト(記号削除ver)
                removed_sign_dst_surface = syntax.chunks[dst_index].surface(remove_sign=True)
                # 係り元、係り先ともに文字列として存在すれば出力
                if removed_sign_src_surface != '' and removed_sign_dst_surface != '':
                    print(removed_sign_src_surface + '\t' + removed_sign_dst_surface)


if __name__ == '__main__':
    main()

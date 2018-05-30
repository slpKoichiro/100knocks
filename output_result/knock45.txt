"""
45. 動詞の格パターンの抽出

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ
ただし，出力は以下の仕様を満たすようにせよ．

    動詞を含む文節において，最左の動詞の基本形を述語とする
    述語に係る助詞を格とする
    述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

仕様:
    動詞を含む文節に係っている文節における、最後の形態素が助詞である場合を対象とした。
    (例) 言うよりも
        言う    動詞,一般,,,連体形-一般,五段-ワア行,言う
        より    助詞,格助詞,,,,,より
        も      助詞,係助詞,,,,,も

        この文節が動詞に係っていたとしたら、最後が「も」という助詞なので対象は「も」

    (例) 言うよりも速く
        言う    動詞,一般,,,連体形-一般,五段-ワア行,言う
        より    助詞,格助詞,,,,,より
        も      助詞,係助詞,,,,,も
        速く    形容詞,一般,,,連用形-一般,形容詞,速い

        この文節が動詞に係っていたとしたら、この場合は助詞が含まれているが、それが最後の出現ではないので
        対象は見つからなかったとする。
"""

from my_package.read_cabocha_file import read_cabocha_file


def search_morph_in_chunk(chunk, word_class, num=None):
    """
    1文節内で指定された品詞に該当する形態素(Morphクラス)のリストを返す
    :param chunk: 文節
    :param word_class: 品詞
    :param num: 探し出す数(未指定ならば全部探す)
    :return: 形態素(Morphクラス)のリスト
    """
    morph_list = []
    find_count = 0
    if num is None:
        num = len(chunk.morphs)
    for morph in chunk.morphs:
        if morph.pos == word_class:
            morph_list.append(morph)
            find_count += 1
            if find_count >= num:
                break
    return morph_list


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)

    find_verb_flag = False  # 動詞を発見したかどうかのフラグ
    for syntax in syntax_structure:  # syntax: 1文
        for chunk in syntax.chunks:  # chunk: 1文節
            t = search_morph_in_chunk(chunk, '動詞', 1)  # 文節内から動詞の形態素を1つ探す
            if t:  # 見つかった場合
                predicate_base = t[0].base  # 動詞の基本形を述語に
                find_verb_flag = True  # 動詞見つかりましたフラグON!!
            if find_verb_flag is True:  # 動詞を含む文節が見つかった場合は
                find_verb_flag = False
                postposition_list = []  # 助詞のリスト
                for src in chunk.srcs:  # 係り元の文節内に助詞があるか探す
                    last_morph = syntax.chunks[int(src)].morphs[-1]  # 文節内の最後の形態素
                    if last_morph.pos == '助詞':  # 文節内の最後の形態素が助詞だったら
                        postposition_list.append(last_morph.surface)  # その表層形をリストに追加
                if postposition_list:  # 動詞にかかる助詞が1つ以上見つかった場合は出力
                    print('{0}\t{1}'.format(predicate_base, ' '.join(postposition_list)))


if __name__ == '__main__':
    main()

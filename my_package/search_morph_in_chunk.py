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

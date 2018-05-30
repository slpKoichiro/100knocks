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

from Morpheme import Morpheme

def main():
    file_name = 'materials/neko.txt.mecab'
    morph = Morpheme(mecab_file_name=file_name)
    result = morph.read_mecab_file()  # 辞書のリスト

    noun_comb = []
    for d in result:
        if d['pos'] == '名詞':
            noun_comb.append(d['surface'])
        elif len(noun_comb) > 1:
            print(''.join(noun_comb))
            noun_comb.clear()
        else:  # 名詞の出現が0 or 1個で途切れたとき
            noun_comb.clear()

    if len(noun_comb) > 1:  # 名詞で終わる文章の場合のケア
        print(''.join(noun_comb))


if __name__ == '__main__':
    main()

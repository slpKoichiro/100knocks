from Morpheme import Morpheme

def main():
    file_name = 'materials/neko.txt.mecab'
    morph = Morpheme(mecab_file_name=file_name)
    result = morph.read_mecab_file()  # 辞書のリスト

    for i, d in enumerate(result[1:], 1):
        if d['surface'] == 'の':
            pre = result[i-1]
            nex = result[i+1]
            if pre['pos'] == nex['pos'] == '名詞':
                print(pre['surface'] + d['surface'] + nex['surface'])


if __name__ == '__main__':
    main()

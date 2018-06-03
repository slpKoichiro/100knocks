"""
54. 品詞タグ付け

(例)
          <token id="1">
            <word>Natural</word>
            <lemma>natural</lemma>
            <CharacterOffsetBegin>0</CharacterOffsetBegin>
            <CharacterOffsetEnd>7</CharacterOffsetEnd>
            <POS>JJ</POS>
            <NER>O</NER>
            <Speaker>PER0</Speaker>

"""

from xml.etree import ElementTree


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()
    for token in root.iter('token'):  # 'token'ノードのみを処理
        word = token.findtext('word')
        lemma = token.findtext('lemma')
        pos = token.findtext('POS')
        print('{0}\t{1}\t{2}'.format(word, lemma, pos))


if __name__ == '__main__':
    main()

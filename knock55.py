"""
55. 固有表現抽出

(例)
          <token id="4">
            <word>Alan</word>
            <lemma>Alan</lemma>
            <CharacterOffsetBegin>636</CharacterOffsetBegin>
            <CharacterOffsetEnd>640</CharacterOffsetEnd>
            <POS>NNP</POS>
            <NER>PERSON</NER>
            <Speaker>PER0</Speaker>

"""

from xml.etree import ElementTree


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()
    for token in root.iter('token'):  # 'token'ノードのみを処理
        ner = token.findtext('NER')  # 人名のみ出力
        if ner == 'PERSON':
            print(token.findtext('word'))


if __name__ == '__main__':
    main()

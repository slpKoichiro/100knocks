"""
53. Tokenization

1) コマンドにて, stanford core NLPを実行. (2分くらいかかるし、動作めっちゃ重くなる)
    $ corenlp -file ./nlp.txt
    (参考URL: http://lab.astamuse.co.jp/entry/corenlp1)

2) https://qiita.com/segavvy/items/ab6bb2b994aac061f51f
    を参考にWEBブラウザーで可視化できるようにして確認.

3) pythonでxmlファイルを読み込むには下記の公式ドキュメントなどを参考にした
    https://docs.python.jp/3/library/xml.etree.elementtree.html
    http://www.digifie.jp/blog/archives/1459

(注) JAVAのバージョンが新しすぎるとエラーが発生するので、JAVA8くらいに落とす必要あり！？
    (参考URL: http://note.kurodigi.com/post-0-2/)
"""

from xml.etree import ElementTree


def main():
    xml_file_path = 'materials/nlp.txt.xml'
    tree = ElementTree.parse(xml_file_path)  # 木構造を生成
    root = tree.getroot()
    for word in root.iter('word'):  # 'word'ノードのみを処理
        print(word.text)  # 'word'ノードの値を出力


if __name__ == '__main__':
    main()

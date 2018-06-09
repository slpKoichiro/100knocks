"""
69. Webアプリケーションの作成

flaskの参考ページ http://d.hatena.ne.jp/yohei-a/20180503/1525366741
他にも、htmlファイルが意味不明だったので, jinja2をググった

(注意) SMAPやAKB48などで検索かけると、全く同じ見た目のテーブルが3つでてきたが
    findとcount使って調べても3と出力されるし,
    _idの値は異なるので実際にファイルに3つ記載してあったものと考えられる.
"""

from knock69_directory.server import main

if __name__ == '__main__':
    main()

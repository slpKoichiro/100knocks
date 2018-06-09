"""
64. MongoDBの構築

参考URL: https://qiita.com/ognek/items/a37dd1cd0e26e6adecaa

端末で
sudo service mongod start
してからプログラム実行しないと怒られる！？
"""

import pymongo
import json


def main():
    client = pymongo.MongoClient()  # mongodb へのアクセスを確立
    db = client.ArtistDB  # データベースを作成 (名前: ArtistDB)
    collection = db.artist  # コレクション(テーブル)を作成 (名前: artist)

    file_name = 'materials/artist.json'
    with open(file_name, 'r', encoding='utf-8') as json_file:
        for line in json_file:  # line: JSON形式のstr型(1つのデータ = "1行の文字列")
            py_data = json.loads(line)  # JSON形式の文字列を辞書型へ
            collection.insert_one(py_data)  # データを登録

    # インデックス作成
    collection.create_index([('name', pymongo.ASCENDING)])
    collection.create_index([('aliases.name', pymongo.ASCENDING)])
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])


if __name__ == '__main__':
    main()

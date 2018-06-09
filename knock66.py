"""
66. 検索件数の取得

公式ドキュメント:
http://api.mongodb.com/python/current/api/pymongo/collection.html
"""

import pymongo


def main():
    # テンプレ
    client = pymongo.MongoClient()  # mongodb へのアクセスを確立
    db = client.ArtistDB  # データベースを作成 (名前: ArtistDB)
    collection = db.artist  # コレクション(テーブル)を作成 (名前: artist)

    # DBに対しての処理
    print(collection.find({'area': 'Japan'}).count())


if __name__ == '__main__':
    main()

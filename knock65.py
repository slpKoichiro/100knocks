"""
65. MongoDBの検索

公式ドキュメント:
http://api.mongodb.com/python/current/api/pymongo/collection.html
"""

import pymongo


def main():
    # テンプレ
    client = pymongo.MongoClient()  # mongodb へのアクセスを確立
    db = client.ArtistDB  # データベースを作成 (名前: ArtistDB)
    collection = db.artist  # コレクション(テーブル)を作成 (名前: artist)

    # dbに対しての処理
    for q in collection.find({'name': 'Queen'}):
        print(q)


if __name__ == '__main__':
    main()

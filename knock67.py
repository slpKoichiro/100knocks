"""
67. 複数のドキュメントの取得

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
    search_name = input('アーティストの別名を入力してください')
    aliases_names = collection.find({'aliases.name': search_name})
    if aliases_names.count() != 0:
        for aliases_name in aliases_names:
            print(aliases_name)
    else:
        print('入力された別名を持つアーティストはいませんでした.')


if __name__ == '__main__':
    main()

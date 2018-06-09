"""
68. ソート

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
    sorted_datas = collection.find({'tags.value': 'dance'}). \
        sort('rating.count', pymongo.DESCENDING)
    for ranking, sorted_data in enumerate(sorted_datas[0:10], 1):
        print('{0}\t{1}'.format(ranking, sorted_data['name']))


if __name__ == '__main__':
    main()

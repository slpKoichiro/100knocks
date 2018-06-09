"""
61. KVSの検索
"""

import plyvel


def main():
    db_name = 'materials/artist.ldb'
    # DBがなければ作る
    db = plyvel.DB(db_name, create_if_missing=True)

    artist_name = input('アーティスト名: ')
    name = artist_name.encode()
    area = db.get(name)
    if area is not None:
        if area != '':
            print('アーティスト名: [{0}], 活動場所: [{1}]'.format(name.decode(), area.decode()))
        else:
            print('アーティスト名: [{0}] の活動場所は登録されていません.'.format(name.decode()))
    else:
        print('アーティスト名: [{0}] はDBに登録されていません.'.format(name.decode()))

    # 最後は閉じる
    db.close()


if __name__ == '__main__':
    main()

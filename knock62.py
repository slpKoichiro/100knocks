"""
62. KVS内の反復処理

plyvelについてのドキュメント:
http://plyvel.readthedocs.io/en/latest/api.html
"""

import plyvel


def main():
    db_name = 'materials/artist.ldb'
    # DBがなければ作る
    db = plyvel.DB(db_name, create_if_missing=True)

    # keyはいらないので、valueだけのイテレーターを得る
    area_jp_num = sum(1 for v in db.iterator(include_key=False) if v == b'Japan')
    print('活動場所がJapanのアーティスト数: {0}'.format(area_jp_num))

    # 最後は閉じる
    db.close()


if __name__ == '__main__':
    main()

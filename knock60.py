"""
60. KVSの構築
"""

import json
import plyvel


def main():
    file_name = 'materials/artist.json'
    db_name = 'materials/artist.ldb'

    # DBがなければ作る
    db = plyvel.DB(db_name, create_if_missing=True)

    with open(file_name, 'r', encoding='utf-8') as json_file:
        for line in json_file:  # line: JSON形式のstr型(1つのデータ = "1行の文字列")
            py_data = json.loads(line)  # JSON形式の文字列を辞書型へ

            key = py_data['name']  # 'name'はすべてのデータが必ず持っている(確認済み)
            if 'area' in py_data.keys():  # 'area'は持っていないデータもある
                value = py_data['area']
            else:
                value = ''  # 'area'が登録されていなかったらとりあえず空文字を入れる

            # データベースに登録する(byte列に変換する必要あり), keyの重複は指定ないので無視
            db.put(key.encode(), value.encode())

    # 最後は閉じる
    db.close()


if __name__ == '__main__':
    main()

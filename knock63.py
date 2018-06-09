"""
63. オブジェクトを値に格納したKVS
"""

import plyvel
import json


def create_tag_db():
    """
    key:アーティスト, value:{非タグ数:回数, タグ名:名称}[]を表すjson文字列を満たすDBを構築する関数
    :return: なし
    """
    file_name = 'materials/artist.json'
    db_name = 'materials/artist_tag.ldb'

    # DBがなければ作る
    db = plyvel.DB(db_name, create_if_missing=True)

    # DB構築
    with open(file_name, 'r', encoding='utf-8') as json_file:
        for line in json_file:  # line: JSON形式のstr型(1つのデータ = "1行の文字列")
            py_data = json.loads(line)  # JSON形式の文字列を辞書型へ
            if 'tags' in py_data.keys():
                key = py_data['name']  # 文字列
                value = py_data['tags']  # {'count:xxx', 'value':yyy}[]
                # リストであるvalueはそのままではencode()できないので、jsonの「文字列」に変換しておく
                dumped_tags = json.dumps(value)
                # データベースに登録する(byte列に変換する必要あり), keyの重複は指定ないので無視
                db.put(key.encode(), dumped_tags.encode())

    # 最後は閉じる
    db.close()


def search_tag():
    """
    上記のDBから入力としてアーティスト名を受け取って、タグを検索する関数
    :return: なし
    """
    db_name = 'materials/artist_tag.ldb'

    # DBがなければ作る
    db = plyvel.DB(db_name, create_if_missing=True)

    # tag検索
    artist_name = input('アーティスト名: ')
    name = artist_name.encode()

    if db.get(name) is not None:
        dumped_tags = db.get(name).decode()
        tags = json.loads(dumped_tags)
        print('アーティスト名: [{0}] のタグ情報が見つかりました.'.format(name.decode()))
        for tag in tags:
            print('\t{0}({1})'.format(tag['value'], tag['count']))
    else:
        print('アーティスト名: [{0}] はDBに登録されていません.'.format(name.decode()))

    # 最後は閉じる
    db.close()


def main():
    # create_tag_db()
    search_tag()


if __name__ == '__main__':
    main()

"""
69. Webアプリケーションの作成

flaskの参考ページ http://d.hatena.ne.jp/yohei-a/20180503/1525366741
他にも、htmlファイルが意味不明だったので, jinja2をググった

(注意) SMAPやAKB48などで検索かけると、全く同じ見た目のテーブルが3つでてきたが
    findとcount使って調べても3と出力されるし,
    _idの値は異なるので実際にファイルに3つ記載してあったものと考えられる.
"""

from flask import Flask, render_template, request
import pymongo


def main():
    # app起動
    app = Flask(__name__)

    # テンプレ
    client = pymongo.MongoClient()  # mongodb へのアクセスを確立
    db = client.ArtistDB  # データベースを作成 (名前: ArtistDB)
    collection = db.artist  # コレクション(テーブル)を作成 (名前: artist)

    # 検索するときのWEBページ
    @app.route('/')
    def form():
        return render_template('form.html')

    # 結果を出力するときのWEBページ
    @app.route('/confirm', methods=['POST', 'GET'])
    def confirm():
        if request.method == 'POST':
            # 辞書型のデータに収められたユーザの入力を処理
            result = request.form
            name = result['name']
            aliases = result['aliases']
            tag = result['tag']

            output_flag = 0  # 検索結果が存在したかどうかのフラグ
            # 複数条件をひろっていく
            find_key = []
            if name != '':
                find_key.append({'name': name})
            if aliases != '':
                find_key.append({'aliases.name': aliases})
            if tag != '':
                find_key.append({'tags.value': tag})
            # 条件が1つ以上入力されたうえで、検索がクリックされていたら
            if find_key:
                # 指定された条件たちのandで検索を行う(pymongoの複数条件はこの書式(google先生より))
                found_datas = collection.find({'$and': find_key})
                # 検索結果が1つ以上見つかった場合は
                if found_datas.count():
                    # ソート
                    sorted_datas = found_datas.sort('rating.count', pymongo.DESCENDING)
                    result = sorted_datas
                    output_flag = 1
            # WEBページの情報と, 検索結果の情報と, 検索結果が存在したかどうかのフラグを渡す
            return render_template("confirm.html", result=result, output_flag=output_flag)

    # app実行
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()

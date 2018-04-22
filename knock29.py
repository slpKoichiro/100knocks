from JsonProcess import JsonProcess
import re
import urllib.request
import urllib.parse
import json


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    sentence = json_pro.search_text('イギリス')
    template_dict = json_pro.extract_template(sentence)

    """
    Wikipedia日本語版の場合、URLは次のようになる。
    http://ja.wikipedia.org/w/api.php?パラメータ1=値1&パラメータ2=値2&...&パラメータn=値n
        format 	出力フォーマット 	json, xml, yaml, ...
        action 	操作 	query, login, logout, edit, ..
        prop 	記事の各構成要素を取得 	info, revisions, categories, links, templates, images, ...
            prop=記事の構成要素を用いる場合、次のいずれかのパラメータを用いて記事を指定する。
                titles 	記事タイトル 	（URLエンコードされた文字列）
                pageids 	記事ID 	（整数）
        
            
    """

    url = 'http://ja.wikipedia.org/w/api.php?'
    url += 'format=json&'
    url += 'action=query&'
    url += 'prop=imageinfo&'
    url += 'titles=File:'+urllib.parse.quote_plus(template_dict['国旗画像'])+'&'  # ファイル名から空白を消す
    url += 'iiprop=url'  # レスポンスに画像のurlを含めさせる

    response = urllib.request.urlopen(url)  # HTTP Responseオブジェクトを返す
    body = response.read() # read()メソッドはbyte文字列を返す. 半角英数字だけなので見た目str型と変わらないが...
    decoded_body = body.decode('utf-8')  # decodeしてbytes型からstr型へ
    data = json.loads(decoded_body)  # 辞書型に変換
    # dataを出力して見ながら, なんとかURLにたどり着いた. すごい入れ子構造になってるので辛かった...
    # 結論: data['query']['pages']['-1']['imageinfo'][0]['url']
    query_data = data['query']
    pages_data = query_data['pages']
    imageinfo_data = pages_data['-1']['imageinfo']
    image_url = imageinfo_data[0]['url']
    print(image_url)


if __name__ == '__main__':
    main()

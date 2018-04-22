from JsonProcess import JsonProcess
import re


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    sentence = json_pro.search_text('イギリス')
    template_dict = json_pro.extract_template(sentence)

    # knock26
    pattern = re.compile(r"'+")
    for k, v in template_dict.items():
        new_v = re.sub(pattern, '', v)
        template_dict[k] = new_v

    # knock28
    # knock27 + Fileも処理に含めるようにpattern変更(':'の修正と(xxx|)の出現回数を0or1から*に)
    # pattern = re.compile(r'\[\[([^|:\]]*?\|)?([^:]*?)\]\]')
    pattern = re.compile(r'\[\[([^|\]]*?\|)*(.*?)\]\]')
    for k, v in template_dict.items():
        new_v = re.sub(pattern, r'\2', v)  # [[xxx|yyy]]or[[yyy]]に一致する文字列をyyyに置換
        template_dict[k] = new_v

    # URLの削除
    # [http://xxx] or [http://xxx yyy] -> yyy
    pattern = re.compile(r'\[http://(\S)*\s(.*?)\]')
    for k, v in template_dict.items():
        new_v = re.sub(pattern, r'\2', v)
        template_dict[k] = new_v

    # br, ref, referenceの削除
    pattern = re.compile(r'</?(br|ref)[^>]*?>')
    for k, v in template_dict.items():
        new_v = re.sub(pattern, '', v)
        template_dict[k] = new_v

    # {{lang|xxx|yyy}} -> yyy
    pattern = re.compile(r'\{\{lang\|([^\|]+?)\|([^\}]*?)\}\}')
    for k, v in template_dict.items():
        new_v = re.sub(pattern, r'\2', v)
        template_dict[k] = new_v


    # print('基礎情報: {0}'.format(template_name))
    for tt in template_dict.items():
        print(tt)


if __name__ == '__main__':
    main()

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

    # knock27
    pattern = re.compile(r'\[\[([^|:\]]*?\|)?([^:]*?)\]\]')
    # [[xxx|yyy]] or [[yyy]]
    # xxx|: [^|\]]*?\| ... '|'と':'と']'以外の文字の連続+'|'. "@[[xxx|yyy]]@[[aaa|bbb]]@"のような複数[[xxx|yyy]]が出るときに失敗する.
    #                      ':'はFILEやCategoryの行を巻き込まないため
    # yyy:  [^:]*?     ... ':'はFILEやCategoryの行を巻き込まないため
    for k, v in template_dict.items():
        new_v = re.sub(pattern, r'\2', v)  # [[xxx|yyy]]or[[yyy]]に一致する文字列をyyyに置換
        template_dict[k] = new_v

    # print('基礎情報: {0}'.format(template_name))
    for tt in template_dict.items():
        print(tt)


if __name__ == '__main__':
    main()

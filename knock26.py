from JsonProcess import JsonProcess
import re


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    sentence = json_pro.search_text('イギリス')
    template_dict = json_pro.extract_template(sentence)

    pattern = re.compile(r"'+")
    for k, v in template_dict.items():
        new_v = re.sub(pattern, '', v)
        template_dict[k] = new_v

    # print('基礎情報: {0}'.format(template_name))
    for tt in template_dict.items():
        print(tt)


if __name__ == '__main__':
    main()

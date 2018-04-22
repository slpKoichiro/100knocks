from JsonProcess import JsonProcess
import re


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    found_sentence = json_pro.search_text('イギリス')
    listed_sentence = found_sentence.split('\n')

    for line in listed_sentence:
        pattern = r'\[\[Category:(?P<BODY>.*?)(\|.*)?]]'
        m = re.search(pattern, line)  # (.*?): 最小マッチの*?記号, (\|.*)?: 0or1回の?記号
        if m:
            print(m.group('BODY'))


if __name__ == '__main__':
    main()
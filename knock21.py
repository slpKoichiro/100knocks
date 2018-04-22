from JsonProcess import JsonProcess
import re


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    found_sentence = json_pro.search_text('イギリス')
    listed_sentence = found_sentence.split('\n')
    for line in listed_sentence:
        m = re.search('Category', line)
        if m:
            print(line)


if __name__ == '__main__':
    main()

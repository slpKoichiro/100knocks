from JsonProcess import JsonProcess
import re


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    found_sentence = json_pro.search_text('イギリス')
    listed_sentence = found_sentence.split('\n')

    for line in listed_sentence:
        """
        [[File:Oil platform in the North SeaPros.jpg|thumb|[[北海油田]]]]
        [[ファイル:The Fabs.JPG|thumb|200px|[[ビートルズ]]]]
        ファイル:PalaceOfWestminsterAtNight.jpg|[[ウェストミンスター宮殿]]
        """
        pattern = re.compile(r'.*?(ファイル|File):(?P<NAME>.*?\..*?)\|.*?')
        m = re.search(pattern, line)
        if m:
            print(m.group('NAME'))


if __name__ == '__main__':
    main()

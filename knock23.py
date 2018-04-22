from JsonProcess import JsonProcess
import re


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    found_sentence = json_pro.search_text('イギリス')
    listed_sentence = found_sentence.split('\n')

    for line in listed_sentence:
        pattern = re.compile(r'(?P<LEFT_EQ>=+)(?P<SECTION>\w+?)(?P<RIGHT_EQ>=+)')  # ==xxx== みたいなの
        # (?P<LEFT_EQ>=+): (?P<LEFT_EQ>=)+だとm.group('LEFT_EQ')は毎回1個の'='で書き換えられて(ループ)結果的に'='1個のみになるのでダメ
        m = re.search(pattern, line)
        if m:
            left_eq = m.group('LEFT_EQ')
            right_eq = m.group('RIGHT_EQ')
            if len(left_eq) == len(right_eq):
                eq_num = len(left_eq)
                print('{0}:\t{1}'.format(m.group('SECTION'), eq_num-1))


if __name__ == '__main__':
    main()
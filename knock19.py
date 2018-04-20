import subprocess
from collections import defaultdict


if __name__ == '__main__':
    with open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        count_dict = defaultdict(int)  # key: 単語(1列目), value: 単語の出現回数
        lines = []
        for l in f:
            line = l.rstrip().split('\t')
            lines.append(line)
            col1 = line[0]  # 単語(1列目)の取得
            count_dict[col1] += 1

    print('[result of python]:')
    # ソートして出力
    for word, count in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
        print('      {1}\t{0}'.format(word, count))

    res = subprocess.check_output(
        'sh -c "cut -f 1 materials/hightemp.txt | sort |uniq -c|sort -r"'
        , shell=True).decode('utf-8')
    print('---------------\n\n[result of UNIX command]:\n{0}'.format(res))


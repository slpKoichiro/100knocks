import subprocess
import sys


if __name__ == '__main__':
    args = sys.argv
    N = int(args[1])

    print('[result of python]:')
    with open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):  # 面倒なのでfileに書き込むことはしなかった
            if i % N:  # N行ごとに別処理
                print(line, end='')
            else:
                print(line, end='-----\n')

    res = subprocess.check_call(['split', '-l', args[1], "materials/hightemp.txt", 'materials/divide-'])\

import subprocess
import sys


if __name__ == '__main__':
    args = sys.argv
    N = int(args[1])  # int()しないと失敗する

    print('[result of python]:')
    with open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        for i in range(N):
            print(f.readline(), end='')

    res = subprocess.check_output(['head', '-n', args[1], "materials/hightemp.txt"])\
        .decode('utf-8')
    print('\n[result of UNIX command]:\n{0}'.format(res))
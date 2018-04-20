import subprocess
import sys


if __name__ == '__main__':
    args = sys.argv
    N = int(args[1])

    print('[result of python]:')
    with open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        [print(line, end='') for line in lines[-N:]]

    res = subprocess.check_output(['tail', '-n', args[1], "materials/hightemp.txt"])\
        .decode('utf-8')
    print('\n[result of UNIX command]:\n{0}'.format(res))
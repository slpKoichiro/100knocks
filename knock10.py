import subprocess


if __name__ == '__main__':
    num_lines = sum(1 for line in open('materials/hightemp.txt', 'r', encoding='utf-8'))
    print('[result of python]: {0}'.format(num_lines))
    res = subprocess.check_output(['wc', 'materials/hightemp.txt']).decode()
    print('[result of UNIX command]: {0}'.format(res))

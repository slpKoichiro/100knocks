import subprocess


if __name__ == '__main__':
    with open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line.rstrip().split('\t'))
        lines.sort(key=lambda col: col[2])  # float()付けなくても比較可能
        print('[result of python]:')
        [print('{0[0]}\t{0[1]}\t{0[2]}\t{0[3]}'.format(line)) for line in lines]


    res = subprocess.check_output(['sort', '-k', '3,3', "materials/hightemp.txt"])\
        .decode('utf-8')
    print('-----\n\n[result of UNIX command]:\n{0}'.format(res))
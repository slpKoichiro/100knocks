import subprocess


if __name__ == '__main__':
    f_col1 = open('materials/col1.txt', 'w', encoding='utf-8')
    f_col2 = open('materials/col2.txt', 'w', encoding='utf-8')
    with open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        for line in f:
            cols = line.split('\t')
            f_col1.write(cols[0] + '\n')
            f_col2.write(cols[1] + '\n')
    f_col1.close()
    f_col2.close()

    res = subprocess.check_output(['cut', '-f', '1,2', "materials/hightemp.txt"])\
        .decode('utf-8')
    print('[result of UNIX command]:\n{0}'.format(res))
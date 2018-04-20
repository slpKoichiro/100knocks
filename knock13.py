import subprocess


if __name__ == '__main__':
    f_col1 = open('materials/col1.txt', 'r', encoding='utf-8')
    f_col2 = open('materials/col2.txt', 'r', encoding='utf-8')
    with open('materials/merge.txt', 'w', encoding='utf-8') as f_merge:
        for line1, line2 in zip(f_col1, f_col2):
            merge_col = line1[:-1] + '\t' + line2[:-1]
            f_merge.write(merge_col + '\n')
    f_col1.close()
    f_col2.close()

    res = subprocess.check_output(['paste', "materials/col1.txt", "materials/col2.txt"])\
        .decode('utf-8')
    print('[result of UNIX command]:\n{0}'.format(res))
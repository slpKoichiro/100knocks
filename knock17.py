import subprocess


if __name__ == '__main__':
    print('[result of python]:')
    with open('materials/col1.txt', 'r', encoding='utf-8') as f:
        word_set = set()
        for line in f:
            elem = line.rstrip()
            word_set.add(elem)
        [print(w) for w in word_set]

    res = subprocess.check_output('sh -c "cat materials/col1.txt| sort | uniq"', shell=True).decode('utf-8')
    print('\n[result of UNIX command]:\n{0}'.format(res))
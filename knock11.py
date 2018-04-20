import subprocess


if __name__ == '__main__':
    with  open('materials/hightemp.txt', 'r', encoding='utf-8') as f:
        original_sentence = f.read()
        replaced_sentence = original_sentence.replace('\t', ' ')
    print('[result of python]:\n{0}'.format(replaced_sentence))
    res = subprocess.check_output(['sed', 's/\t/ /g', "materials/hightemp.txt"]).decode('utf-8')
    print('[result of UNIX command]:\n{0}'.format(res))

    if replaced_sentence == res:
        print('matching result!!')
    else:
        print('not matching.')

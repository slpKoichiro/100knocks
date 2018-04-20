import re

if __name__ == '__main__':
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
               "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = re.findall(r'\w+', sentence)

    word_dict = {}
    first_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for i, w in enumerate(words, 1):
        if i in first_list:
            word_dict[w[:1]] = i
        else:
            word_dict[w[:2]] = i

    print(word_dict)
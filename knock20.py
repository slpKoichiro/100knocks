from JsonProcess import JsonProcess


def main():
    file_name = 'materials/jawiki-country.json'
    json_pro = JsonProcess(file_name)
    found_sentence = json_pro.search_text('イギリス')
    print(found_sentence)


if __name__ == '__main__':
    main()

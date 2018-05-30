"""
41. 係り受け解析結果の読み込み（文節・係り受け）
"""

from my_package.read_cabocha_file import read_cabocha_file


def main():
    output_file_name = 'materials/neko.txt.cabocha'
    syntax_structure = read_cabocha_file(output_file_name)
    syntax_structure[7].output()


if __name__ == '__main__':
    main()

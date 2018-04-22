"""
{"text": "{JSON形式の記事本文}", "title": "記事名"}

"""

import json
import re
from collections import OrderedDict


class JsonProcess(object):
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name

    def search_text(self, title):
        with open(self.file_name, 'r', encoding='utf-8') as json_file:
            for line in json_file:  # line: JSON形式のstr型(1つのデータ = "1行の文字列")
                py_data = json.loads(line)  # JSON形式の文字列を辞書型へ
                if py_data['title'] == title:
                    return py_data['text']

    @classmethod
    def extract_template(cls, sentence):
        pattern1 = re.compile(r'\{\{基礎情報 (?P<TEMPLATE>.*)\n(?P<BODY>(.*\n)*)\}\}')
        m1 = re.search(pattern1, sentence)
        template_name = m1.group('TEMPLATE')  # 国名
        template_body = m1.group('BODY')  # テンプレートの中身 {{xxx}}

        tmp = template_body.rstrip().replace('\n*', '*')  # '*'スタートのものを連結('\n'を削除)
        listed_body = tmp.split('\n')  # listed_body = '|xxx = yyy'のリスト

        # '*'スタートについて, 削除した'\n'を再度付与(イギリスの場合は公式国名の行のため)
        listed_body2 = []
        for t in listed_body:
            tt = re.sub(r'(?<!\*)\*', r'\n*', t)
            listed_body2.append(tt)

        template_dict = OrderedDict()
        pattern2 = re.compile(r'\|(?P<KEY>.*) = (?P<VALUE>(.|\n)*)')  # |key = value
        for t in listed_body2:
            m2 = re.search(pattern2, t)
            key = m2.group('KEY')
            val = m2.group('VALUE')
            template_dict[key] = val
        """
        print('基礎情報: {0}'.format(template_name))
        for tt in template_dict.items():
            print(tt)
        """
        return template_dict

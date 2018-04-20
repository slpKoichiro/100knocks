import re


class Ngram(object):
    def __init__(self, sample):
        self._sample = sample

    @property
    def sample(self):
        return self._sample

    @sample.setter
    def sample(self, sample):
        self._sample = sample

    def make_word_ngram(self, n):
        words = re.findall(r'\w+', self.sample)
        word_ngram = set()
        gram_num = len(words) - n + 1   # number of n-gram
        for i in range(gram_num):
            word_ngram.add(' '.join(words[i:i+n]))  # elements in list "words" are joined with space
        return word_ngram

    def make_char_ngram(self, n):
        characters = re.findall(r'\w', self.sample)
        char_ngram = set()
        gram_num = len(characters) - n + 1  # number of n-gram
        for i in range(gram_num):
            char_ngram.add(''.join(characters[i:i+n]))  # elements in list "characters" are joined simply
        return char_ngram


if __name__ == '__main__':
    gram1 = Ngram("I am an NLPer")
    bi_word_gram = gram1.make_word_ngram(2)
    bi_char_gram = gram1.make_char_ngram(2)
    print(bi_word_gram)
    print(bi_char_gram)


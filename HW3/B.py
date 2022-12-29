import nltk


class FileReader:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'{self.path}'

    def read(self):
        try:
            with open(self.path, encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return []

    def count(self):
        line_count = 0
        word_count = 0
        for line in open(self.path):
            line_count += 1
            word_count += len(nltk.wordpunct_tokenize(line))
        return line_count, word_count




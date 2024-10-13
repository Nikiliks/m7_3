import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        sim = [',', '.', '=', '!', '?', ';', ':', ' - ']
        alternative_sim =''
        for file_names in self.file_names:
            with open(file_names, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for i in line:
                        if i in sim:
                            line = line.replace(i, '')
                    alternative_sim += line
                all_words.update({self.file_names:alternative_sim.split()})
                return all_words

    def find(self, word):
        dict_ = {}
        for self.file_names, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    dict_.update({self.file_names: i + 1})
                    return dict_

    def count(self, word):
        dict_ = {}
        for self.file_names, words in self.get_all_words().items():
            dict_.update({self.file_names: words.count(word.lower())})
            return dict_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего










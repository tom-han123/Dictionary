import csv
import pyttsx3

class Dictionary:
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang

    def word_definition(self):
        file = f'data/fruits.csv'
        data = {}
        if self.lang == 'eng':
            with open(file, 'r', encoding='UTF-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        data[row[0].lower()] = row[1]
        elif self.lang == 'ch':
            with open(file, 'r', encoding='UTF-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        data[row[1]] = row[0].lower()
        if word in data.keys():
            return data[self.word]
        return

class TexttoSpeech:
    def __init__(self, text, lang):
        self.text = text
        self.lang = lang

    def to_speech(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 100)
        voices = engine.getProperty('voices')
        if self.lang == 'ch':
            engine.setProperty('voice', voices[1].id)
        elif self.lang == 'eng':
            engine.setProperty('voice', voices[2].id)
        engine.say(self.text)
        engine.runAndWait()

if __name__ == '__main__':
    while True:
        more = input('Do you have any word to search?(y/n)...')

        if more == 'y' or more == 'Y':
            word = input('Enter the word you want to search...')
            lang = ''
            if word.upper() != word.lower():
                lang = 'eng'
            else:
                lang = 'ch'
            d = Dictionary(word, lang)
            text = d.word_definition()
            print(word + " ==> " + text)
            if text is None:
                speech = TexttoSpeech('There is no such word in this dictionary', 'eng')
            else:
                speech = TexttoSpeech(text, lang)
            speech.to_speech()
        else:
            break

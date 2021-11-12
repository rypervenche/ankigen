<<<<<<< HEAD
import re
class Word:
    def __init__(self, simplified, pinyin, definitions, cn_sentence, eng_sentence):
        self.simplified = simplified.strip()
        self.pinyin = pinyin.strip()
        self.cn_sentence = cn_sentence.strip()
        self.eng_sentence = eng_sentence.strip()
        self.definitions = definitions
    def printDescription(self):
        print(f"The word {self.simplified} ({self.pinyin}) has the following definitions:")
        for definition in self.definitions:
            print(definition.strip())
        if self.cn_sentence and self.eng_sentence:
            print(f"Example sentence:\nCN: {self.cn_sentence}\nEN: {self.eng_sentence}")
dictionary = {}
with open("cedict_tatoeba_userdict.txt", encoding = "utf-8") as tatoeba:
    for line in tatoeba:
        tabsplit = line.split("\t")
        characters = tabsplit[0]
        simplified = characters.split("[")[0]
        #trad = characters.split("[")[1]
        pinyin = tabsplit[1]
        definitions_sentences = tabsplit[2].split("")
        definitions = definitions_sentences[0].split("")
        def_list = []
        for word in definitions:
            def_list.append(word.rstrip())

        if(len(definitions_sentences) > 1):
            sentence_split = definitions_sentences[1].split("")
            cn_sentence = sentence_split[0]
            eng_sentence = sentence_split[1]
            entry = Word(simplified, pinyin, definitions, cn_sentence, eng_sentence)
        else:
            entry = Word(simplified, pinyin, definitions, '', '')
        dictionary[entry.simplified] =  entry

while True:
    word = input("Enter a word: ")
    if dictionary.get(word):
        dictionary[word].printDescription()
    else:
        print(f"We couldn't find an entry for {word} on tatoeba.")


        
        
=======
import re
class Word:
    def __init__(self, simplified, pinyin, definitions, cn_sentence, eng_sentence):
        self.simplified = simplified
        self.pinyin = pinyin
        self.cn_sentence = cn_sentence
        self.eng_sentence = eng_sentence
        self.definitions = definitions
dictionary = {}
with open("C:\\Users\\Nosh\\Downloads\\cedict_tatoeba_userdict.txt", encoding = "utf-8") as tatoeba:
    for line in tatoeba:
        tabsplit = line.split("\t")
        characters = tabsplit[0]
        simplified = characters.split("[")[0]
        #trad = characters.split("[")[1]
        pinyin = tabsplit[1]
        definitions_sentences = tabsplit[2].split("")
        definitions = definitions_sentences[0].split("")
        def_list = []
        for word in definitions:
            def_list.append(word.rstrip())

        if(len(definitions_sentences) > 1):
            sentence_split = definitions_sentences[1].split("")
            cn_sentence = sentence_split[0]
            eng_sentence = sentence_split[1]
            entry = Word(simplified, pinyin, definitions, cn_sentence, eng_sentence)
        else:
            entry = Word(simplified, pinyin, definitions, '', '')
        dictionary[entry.simplified] =  entry
with open("C:\\Users\\Nosh\\Downloads\\blaz.txt", encoding = "latin1") as bla:
    for line in bla:
        print(line)

        
        
>>>>>>> 4f8951bc80f65e666614360a1a60b2d6abf47bea
        
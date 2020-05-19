from src.VocabLoader import VocabLoader
from src.string_matcher.Kmp import Kmp
from src.string_matcher.Bm import Bm
from src.string_matcher.Regex import Regex

class Translator(VocabLoader):
    def __init__(self, title, language):
        super().__init__("src/vocabulary/" + language + ".txt")
        self.title = title
        self.language = language
        self.hist = []
    
    def getWordTranslation(self, word : str):
        self.method.setPattern(word)
        for dataTuple in self.datas:
            wordFromDatabase = dataTuple[0]
            if(self.method.isWordMatch(wordFromDatabase)):
                return dataTuple[1]
        return word

    def setMethod(self, methodName):
        if(methodName == 'KMP'):
            self.method = Kmp('')
        elif(methodName == 'BM'):
            self.method = Bm('')
        elif(methodName == 'REGEX'):
            self.method = Regex('')

    def getTranslation(self, sentence : str):
        self.hist.append(sentence)
        words = [word.strip() for word in map(lambda x: x.strip(".,") ,sentence.split())]
        specialCharacter = ("?", "!", "\"")
        for i in range(len(words)):
            if(words[i].endswith(specialCharacter)):
                lastCharIndex = len(words[i]) - 1
                char = words[i][lastCharIndex]
                words[i] = words[i][:lastCharIndex]
                words.insert(i + 1, char)
        translatedSentence = ""
        for word in words:
            translatedWord = self.getWordTranslation(word)
            if(translatedWord == None):
                translatedSentence += word
            else:
                translatedSentence += translatedWord
            translatedSentence += " "
        return translatedSentence.strip();

    def fromSentence(self):
        return self.hist.pop()
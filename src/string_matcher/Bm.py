from src.string_matcher.PatternReader import PatternReader

class Bm(PatternReader):
  def __init__(self, pattern : str):
    return super(Bm, self).__init__(pattern)

  def isWordMatch(self, word : str) :
    if(len(self.getPattern()) != len(word)):
        return False
    wordLength = len(word)
    patternLength  = len(self._pattern)
    patternLastIndex = patternLength - 1
    lastOccurences = self.__getLastOccurences(word)

    i = patternLastIndex #indeks terakhir pattern
    j = patternLastIndex

    if(wordLength < patternLength):
      return False
    while( i < wordLength):
      if(self._pattern[j] == word[i]):
        if(j == 0):
          return True
        else:
          i -= 1
          j -= 1
      else:
        lastOccurence = lastOccurences[word[i]] 
        i = i + patternLength - min(j, lastOccurence + 1);
        j = patternLastIndex
    
    return False

  def __getLastOccurences(self, sentence : str) :
    occurenceDict : dict= { }
    for char in sentence:
      if(not occurenceDict.__contains__(char)):
        occurenceDict[char] = self._pattern.rfind(char)
    return occurenceDict
    
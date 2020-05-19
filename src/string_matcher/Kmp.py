from src.string_matcher.PatternReader import PatternReader

class Kmp(PatternReader):
  def __init__(self, pattern):
    super(Kmp, self).__init__(pattern)

  def isWordMatch(self, word : str):
    if(len(self.getPattern()) != len(word)):
        return False
    isMatchFound = False
    wordLength = word.__len__()
    kmpBorder = self.__getKmpBorder()
    lastPatternCharacterIndex = len(self._pattern)  - 1
    i = 0
    j = 0
    while(not isMatchFound and i < wordLength) :
      mismatchOccured =  (self._pattern[j] != word[i])
      if(mismatchOccured) :
        if(j == 0):
          i+= 1
          continue
        j = kmpBorder[j]
      else:
        patternMatches = (j == lastPatternCharacterIndex)
        if(patternMatches) :
          isMatchFound = True
        else :
          j += 1
          i += 1
    return isMatchFound

  
  def __getKmpBorder(self):
    """
      hasil dari fungsi ini akan berupa matrix seperti berikut:
      pattern : a b a b b
      k       : 0 0 1 2 3
      b(k)    : 0 0 1 2 0
    """
    kmpBorderSize = len(self._pattern)
    kmpBorder : list = [0 for i in range(kmpBorderSize)]
    if(kmpBorderSize <= 1):
      return kmpBorder
    else:
      for j in range(1, kmpBorderSize):
        suffixes = self.__getSuffixes(j)
        prefixes = self.__getPrefixes(j)
        for i in reversed(range(len(suffixes))):
          if(suffixes[i] == prefixes[i]):
            kmpBorder[j] = i + 1
            break
      return kmpBorder


  def __getSuffixes(self, k) :
    suffixes : list = []
    for i in reversed(range(k)):
      """
        python treat string as : a b c d a b c
        with index               0 1 2 3 4 5 6
        and string[1:2] : means substring starting from index 1, ends before index 2 , which returns ['b']
      """
      startIndex = i + 1
      endIndex   = k + 1
      suffixes.append(self._pattern[startIndex : endIndex])
    return suffixes 

  def __getPrefixes(self, k) :
    prefixes : list = []
    for i in range(k):
      startIndex = 0
      endIndex = i + 1
      prefixes.append(self._pattern[startIndex : endIndex])
    return prefixes
  

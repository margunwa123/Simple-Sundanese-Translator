import re
from src.string_matcher.PatternReader import PatternReader

class Regex(PatternReader):
    def __init__(self, pattern):
        return super(Regex, self).__init__(pattern)

    def isWordMatch(self, word):
        if(len(self.getPattern()) != len(word)):
            return False
        if(bool(re.match(self._pattern, word))):
            return True
        return False


import re

class PatternReader:
  def __init__(self, pattern : str):
    self._pattern : str = pattern

  def getPattern(self):
    return self._pattern
  
  def setPattern(self, pattern : str):
    self._pattern = pattern
  

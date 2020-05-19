class VocabLoader:
    """
    This class is used to load the data using filename and then get the translation of a word
    """
    def __init__(self, fileName : str):
        datas = open(fileName).readlines()
        self.datas = [list(map(lambda x: x.strip() ,data.split("="))) for data in datas]
    
    def getDatas(self):
        return self.datas
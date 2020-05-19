class TehManager:
    """
        Teh Adder digunakan untuk menambahkan teh setelah kata ganti orang
        dalam bahasa sunda
    """
    kataGantiOrang = ["pribados", "urang", "aing", "abdi", "dewek",\
        "kaula", "kuring", "anjeun", "hidep", "maneh", "sia", "anjeunna",\
        "manehna"]
    uselessWord = ["atuh", "mah", "tuman"]
    def useTeh(sentence):
        """
            menambahkan teh terhadap suatu kalimat , tepatnya setelah
            sebuah kata ganti orang
        """
        newSentence = [word.strip() for word in sentence.split()]
        i = 0
        while(i < len(newSentence)):
            if(newSentence[i] in TehManager.kataGantiOrang):
                newSentence.insert(i+1, "teh")
                i += 1
            i += 1
        result = ""
        for word in newSentence:
            result += word + " "
        return result.strip()

    def deleteUselessWord(sentence):
        """
            menghapus teh dari suatu kalimat bila teh ada setelah
            kata ganti orang
        """
        newSentence = [word.strip() for word in sentence.split()]
        i = 0
        while(i < len(newSentence)):
            if(newSentence[i] in TehManager.kataGantiOrang):
                try:
                    if(newSentence[i + 1] == 'teh'):
                        newSentence.pop(i+1)
                except IndexError as error: # kalo udah di index terakhir, diemin
                    pass
            elif(newSentence[i] in TehManager.uselessWord):
                newSentence.pop(i)
            i += 1
        result = ""
        for word in newSentence:
            result += word + " "
        return result.strip()
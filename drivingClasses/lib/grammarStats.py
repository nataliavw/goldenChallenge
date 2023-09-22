class GrammarStats:
    def __init__(self):
        self.resultList = []
        pass

    def check(self, text):
        legalPunct = [".", "?", "!"]

        if text[0].isupper() == True and text[-1] in legalPunct:
            self.resultList.append(True)
            return True
        else:
            self.resultList.append(False)
            return False
    
    def percentage_good(self):
        count = 0
        for result in self.resultList:
            if result == True:
                count += 1
        result = (count / len(self.resultList)) * 100
        return result
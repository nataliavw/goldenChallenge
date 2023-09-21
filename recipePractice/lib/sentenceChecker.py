def sentenceChecker(sentence):
    legalPunct = [".", "?", "!"]

    if sentence[0].isupper() == True and sentence[-1] in legalPunct:
        return True
    else:
        return False
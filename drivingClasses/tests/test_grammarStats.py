from lib.grammarStats import *

def test_no_punctuation_or_cap():
    tester = GrammarStats()
    assert tester.check("no") == False

def test_no_punctuation():
    tester = GrammarStats()
    assert tester.check("No") == False

def test_no_cap():
    tester = GrammarStats()
    assert tester.check("no.") == False

def test_period():
    tester = GrammarStats()
    assert tester.check("Yes.") == True

def test_question():
    tester = GrammarStats()
    assert tester.check("Yes?") == True

def test_exclaimation():
    tester = GrammarStats()
    assert tester.check("Yes!") == True



def test_three_quarters_good_percentage():
    tester = GrammarStats()
    tester.check("no")
    tester.check("Yes.")
    tester.check("Yes.")
    tester.check("Yes.")
    assert tester.percentage_good() == 75

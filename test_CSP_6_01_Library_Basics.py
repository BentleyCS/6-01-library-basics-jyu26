import CSP_6_01_Library_Basics as HW

def test_process_expenses():
    assert HW.process_expenses([1,10,20])== ([1.15, 11.5, 23])

def test_analyze_score():
    assert HW.analyze_scores([2,4,6,9,8,4,2]) == (9,5.0)

def test_sanitize_usernames():
    assert HW.sanitize_usernames(["hi "," bye ","Hello", "apples", "Tree", "Hilarious"]) == (["hi","bye","hello", "apples", "tree", "hilarious"])

def test_identify_outliers():
    assert HW.identify_outliers([5, 1200, 99, 100, -20, 4.5, 200, 247]) == ([1200, 200, 247])

def test_search_and_report():
    assert HW.search_and_report([" Apples", "baT ", "Carrot", "dOG"], "bat", True) ==(1)
    assert HW.search_and_report(["Car ", "Tiger", " poTato", "cardboard "], "potato", False) == (2)
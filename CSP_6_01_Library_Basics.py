import analytics as A
#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    for i in range(len(rawPrices)):
        rawPrices[i] = A.apply_markup(rawPrices[i], 0.15)

    return rawPrices



# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    return A.get_highest(n), A.get_average(n)


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(word_List):
   return A.clean_text(word_List)


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(n: list):
    return A.filter_threshold(n, 100)



# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case worsd with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(item_list, item, is_sorted:bool):
    clean_items = A.clean_text(item_list)
    if is_sorted:
        pos, cnt = A.binarySearch(clean_items, item)
    else:
        pos, cnt = A.linearSearch(clean_items, item)

    return pos

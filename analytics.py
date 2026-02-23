def get_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def get_highest(numbers):
    return max(numbers) if numbers else 0

def apply_markup(price, percentage):
    return price * (1 + percentage)

def clean_text(words_list):
    cleaned_list = []
    for word in words_list:
        clean_word = word.strip().lower()#Deletes whitespace from each end and make lowercase
        cleaned_list.append(clean_word)
    return cleaned_list

def filter_threshold(numbers, limit):
    filtered_results = []
    for n in numbers:
        if n > limit:
            filtered_results.append(n)
    return filtered_results



def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    cnt = 0
    l = 0
    r = len(items)-1

    while(True):
        cnt+=1
        mid = l+ int((r-l)/2)
        if items[mid]== target:
            return mid, cnt
        elif items[mid] < target:
            l=mid+1
        else:
            r=mid-1
        if r < l:
            return -1,cnt



def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.

    for i in range(0, len(items)):
        if items [i] == target:
            return i, i+1

    return -1, i+1
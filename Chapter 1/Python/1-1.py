from collections import Counter

def uniqueChars(string):
    
    counter = Counter()

    for x in string:
        if counter[x] == 1:
            return False
        else:
            counter[x] += 1

    return True


def uniqueChars_sort(string):

    sorted_string = sorted(string)

    for x in range(len(sorted_string)-1):
        if sorted_string[x] == sorted_string[x+1]:
            return False

    return True





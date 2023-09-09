import re


def count_words(string):
    regular = r'\w'
    array = []
    dictionary = {}
    string = string.lower()
    array = string.split(' ')
    for i in range(len(array)):
        if re.match(regular, array[i]):
            array[i] = re.sub(r',','',array[i])
            tmp = array[i]
            if tmp in dictionary:
                dictionary[tmp] += 1
            else:
                dictionary[tmp] = 1
    
    return dict(dictionary)


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
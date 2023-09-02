import re


def combine_anagrams(words_array):
    new_double_array = []
    for i in words_array:
        new_array = []
        tmp_str = []
        for k in i:
            tmp_str.append(k)
        tmp_chars = rf'{tmp_str}' + '{' + rf'{len(tmp_str)}' + '}()' 
        for j in words_array:
            if re.match(tmp_chars, j):
                new_array.append(j)
        if new_array not in new_double_array:
            new_double_array.append(new_array)
        else:
            continue
    return new_double_array

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))

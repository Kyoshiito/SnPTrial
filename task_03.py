def max_odd(array):
    tmp_array = []
    if not array:
        return None
    for j in array:
        if isinstance(j, (int,float)) and round(j) % 2 != 0:
            tmp_array.append(round(j))
    if not tmp_array:
        return None
    else:
        return max(tmp_array)


print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4]))

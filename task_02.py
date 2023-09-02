def coincidence(in_list=[], in_range=range(1,1)):
    result = []
    if in_list == [] and in_range == range(1, 1):
        return result
    for number in in_list:
        if isinstance(number, (int, float)) and round(number) in in_range:
            result.append(number)
    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))

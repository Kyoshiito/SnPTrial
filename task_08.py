import re


def multiply_numbers(inputs = ''):
    multi = 1
    sub_chars = r'\D'
    if inputs == '':
        return None
    else:
        if isinstance(inputs, (int, float)):
            inputs = f'{inputs}'
            inputs = re.sub(sub_chars,'', inputs)
        if isinstance(inputs, str):
            inputs = re.sub(sub_chars,'',inputs)
        inputs = list(inputs)
        if inputs == []:
            return None
        for i in inputs:
            if isinstance(i, str):
                i = int(i)
            multi *= i
        if multi == 1:
            return None
        return multi


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
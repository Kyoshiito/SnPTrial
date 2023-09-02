def check_values(diction):
    final = {}
    for key,value in diction.items():
            if value >= 10:
                final[key] = value
    
    return dict(final)


def connect_dicts(dict1, dict2):
    final_dict = {}
    total1 = sum(dict1.values())
    total2 = sum(dict2.values())

    if total1 > total2:
        final_dict.update(check_values(dict2))
        final_dict.update(check_values(dict1))
        final_dict = sorted(final_dict.items(), key=lambda x: x[1])
    else:
        final_dict.update(check_values(dict1))
        final_dict.update(check_values(dict2))
        final_dict = sorted(final_dict.items(), key=lambda x: x[1])
    return dict(final_dict)


print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))
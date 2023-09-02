def sort_list(in_list):
    tmp_list = []
    if not in_list:
        return []

    for j in range(len(in_list)):
        if isinstance(in_list[j], str):
            continue
        else:
            tmp_list.append(in_list[j])

    max_num_in_list = max(tmp_list)
    min_num_in_list = min(tmp_list)

    for i in range(len(in_list)):
        if in_list[i] == max_num_in_list:
            in_list[i] = min_num_in_list
        elif in_list[i] == min_num_in_list:
            in_list[i] = max_num_in_list
        elif isinstance(in_list[i], str):
            continue
    in_list.append(min_num_in_list)
    return in_list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))

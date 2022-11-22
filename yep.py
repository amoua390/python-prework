def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([0, 1, 5, 13, 22]))
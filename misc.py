def print_dictionary(dict_in):
    for key in dict_in:
        print(key, ': ', dict_in[key])

def is_sorted(input_list):
    for x in range(len(input_list)-1):
        if input_list[x] > input_list[x+1]:
            return False
    return True


# exp1 = [-10, -5, -3, -1, 0, 5, 8, 10]
# exp2 = [-5, -10, 0, -3, 8, 5, -1, 10]

# print(is_sorted(exp1))
# print(is_sorted(exp2))
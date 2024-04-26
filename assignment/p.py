def replace_last_value(tuples_list, new_value):
    modified_list = []
    for tup in tuples_list:
        modified_list.append(tup[:-1] + (new_value,))
    return modified_list

# Example usage:
original_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
modified_list = replace_last_value(original_list, new_value)
print("Original list:", original_list)
print("Modified list:", modified_list)

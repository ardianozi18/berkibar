# solusi tanpa menggunakan set
def remove_duplicate(obj_list):
    new_list = []
    for item in obj_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

# solusi dengan menggunakan set
def remove_duplicate_with_set(obj_list):
    new_list = []
    for set in obj_list:
        if set not in new_list:
            new_list.append(set)
    return new_list

obj_list = [1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6]
print(remove_duplicate(obj_list))
print(remove_duplicate_with_set(obj_list))
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common_elements  = list(set1.intersection(set2))

    return common_elements

l1 = [1, 2, 3]
l2 = [3, 4]

result = find_common_elements(l1, l2)
print(result)
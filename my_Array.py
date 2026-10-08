# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# arr += 7
# print(arr)

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# print(arr1 + arr2)

# print(np.sum(arr))
# print(np.mean(arr))

# arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr3)

# my_list = [3, 1, 4, 1, 5, 9, 2]
# my_list.append(13)
# my_list.insert(3,4)
# my_list.remove(4)
# my_list.sort()
# print(my_list)

# my_dict = {'name': 'John', 'age': 25}
# print(my_dict)
# print(my_dict['name'])
# print(my_dict['age'])

# my_dict['age'] = 32
# print(my_dict['age'])

# my_dict['city'] = 'Kyiv'
# print(my_dict)

# del my_dict['age']
# print(my_dict)

my_set = set([ 2, 4, 3, 5])
my_set.add(1)
my_set.remove(4)
print(my_set) 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}


# def get_first_item(items):
#     return items[0]
# # Завжди виконується одна операція, незалежно від розміру списку

# print(get_first_item([1, 2, 3, 4, 5]))

# def print_all_items(items):
#     for item in items:
#         print(item)
# # Кількість операцій прямо пропорційна кількості елементів у списку

# print_all_items([1, 2, 3, 4, 5])

def dot_product(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))

def get_orthogonal_pairs(vectors):
    n = len(vectors)
    orthogonal_pairs = []

    for i in range(n):
        for j in range(i+1, n):
          if dot_product(vectors[i], vectors[j]) == 0:
            orthogonal_pairs.append((i, j))

    return orthogonal_pairs

vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
print(get_orthogonal_pairs(vectors))

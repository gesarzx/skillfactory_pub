# Сортировка выбором
# На каждом шаге мы имеем отсортированную (слева) и неотсортированную часть (справа).
# Ищется минимальный элемент в неотсортированной части и меняется местами с элементом
# в начале неотсортированной части. И так продолжается, пока не закончится внешний цикл.
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(count)


# Задание 17.8.3
# Задание на самопроверку.
#
# Модифицируйте описанный алгоритм для сортировки по убыванию.
for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]
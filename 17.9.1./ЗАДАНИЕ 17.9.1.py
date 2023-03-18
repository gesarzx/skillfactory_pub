while True:
    num = input("Введите число, равное последовательности чисел: ")
    if num.isnumeric() == True: #проверка что ввели верное число
        num=int(num)
        break
    else:
        print("Это не правильный ввод. Это не длинна последовательности чисел, введите корректное число.")

while True:
    string = input("Введите числа последовательности  через пробел:")
    list_of_strings = string.split()
    list_of_numbers = list(list_of_strings)  # Преобразование введённой последовательности в список

    if not all(numbers.isnumeric() for numbers in list_of_numbers): #проверка что ввели числа
        print("Это не правильный ввод. Это не числа, попробуйте еще раз.")
    else:
        break

list_of_numbers = list(map(int, list_of_numbers))


def qsort(array: object) -> object:  # Сортировка списка по возрастанию элементов в нем
    for i in range(len(array)):

        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

list_of_numbers =qsort(list_of_numbers)
print('отсортированный список:', list_of_numbers)


def bin_search(array, element, left=0, right=len(list_of_numbers)-1):

    if left > right:  # если левая граница превысила правую,
        return right

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        i = middle
        while i > 0 and array[i-1] == element: # обработка случая когда число в списке встречается несколько раз
            i = i-1
        else:
            return i-1

    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return bin_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return bin_search(array, element, middle + 1, right)

print('номер позиции элемента, который меньше введенного пользователем числа:',bin_search(list_of_numbers, num))
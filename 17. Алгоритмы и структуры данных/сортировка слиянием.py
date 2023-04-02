
def merge_sort(L): # "разделяй"
    if len(L) < 2: # если кусок массива меньше 2,
        return L[:] # выходим из рекурсии
    else:
        middle = len(L) // 2 # ищем середину
        left = merge_sort(L[:middle]) # рекурсивно делим левую часть
        right = merge_sort(L[middle:]) # и правую
        return merge(left, right) # выполняем слияние

def merge(left, right): # "властвуй"
    result = [] # результирующий массив
    i ,j = 0 ,0 # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
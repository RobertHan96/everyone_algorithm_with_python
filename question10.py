# 병합정렬 Merge Sort
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    arrary1 = [merge_sort(a[:mid])]
    arrary2 = [merge_sort(a[mid:])]
    result = []

    while arrary1 and arrary2:
        if arrary1[0] < arrary2[0]:
            result.append(arrary1.pop(0))
        else:
            result.append(arrary2.pop(0))
    while arrary1:
        result.append(arrary1.pop(0))
    while arrary2:
        result.append(arrary2.pop(0))
    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))

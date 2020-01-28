# 선택 정렬 알고리즘
def sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        print(a)


d = [2, 4, 5, 1, 3]
sort(d)
print(d)

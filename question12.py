# 이분 탐색
d = [1, 4, 9, 16, 25, 36, 49, 64, 81]


# def binary_search1(a, x):
#     start = 0
#     end = len(a) - 1

#     while start <= end:
#         mid = (start - end) // 2
#         if x == a[mid]:
#             return mid
#         elif x > a[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1


# print(binary_search1(d, 81))


def binary_search2_usb(a, x, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search2_usb(a, x, mid+1, end)
    else:
        return binary_search2_usb(a, x, start, mid-1)
    return -1


def binary_search2(a, x):
    return binary_search2_usb(a, x, 0, len(a)-1)


print("찾는 값의 배열내 위치 : ", binary_search2(d, 50))

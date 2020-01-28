# 1~n까지 수의 합을 구하는 함수를 재귀호출로 만드시오
def solution(num):
    if num == 0:
        return 0
    return num + solution(num-1)


# 숫자 n개 중 최대값을 찾는 함수를 재귀호출로 만드시오
temp = [17, 92, 18, 33, 58, 7, 33, 42]


def solution2(list, n):
    if n == 1:
        return list[0]
    max = solution2(list, n-1)
    if max > list[n-1]:
        return max
    else:
        return list[n-1]


print(solution2(temp, len(temp)))


def solution3(n):
    if n <= 1:
        return n
    return solution3(n-2) + solution3(n-1)


print(solution3(7))


def solution4(n, fromCol, lastCol, suportCol):
    if n == 1:
        print(fromCol, "=>", lastCol)
        return
    solution4(n-1, fromCol, suportCol, lastCol)
    print(fromCol, "=>", lastCol)
    solution4(n-1, suportCol, lastCol, fromCol)


solution4(2, 1, 3, 2)

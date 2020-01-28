# 1~n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for문으로 구현
# 이떄의 시간복잡도는 O(n)


def solution(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 2
    return sum

# for문을 이용하지 않고 제곱의 합을 구하는 공식을 이용하면 간편하게 구하고,
# 시간복잡도 또한 O(1)로 급감함


def solution2(n):
    answer = (n*(n+1)*(n*2+1)) // 6
    return answer


print(solution2(10))

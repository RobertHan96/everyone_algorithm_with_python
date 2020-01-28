# 리스트내 수에서 가장 큰 수의 인덱스값을 구하는 함수를 작성하시오
temp = [17, 92, 18, 33, 58, 7, 33, 42]


def solution(list):
    answer = 0
    for i in range(1, len(list)):
        if list[i] > list[answer]:
            answer = i
    return answer

# 리스트내 수에서 가장 작은 수를 구하는 함수를 작성하시오


def solution2(list):
    answer = list[0]
    for i in range(1, len(list)):
        if list[i] < answer:
            answer = list[i]
        return answer


print(solution2(temp))

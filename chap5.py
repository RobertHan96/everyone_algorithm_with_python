# 리스트에서 원하는 값이 있는 위치를 출력하는 함수를 만드시오
# 같은 값이 중복해서 있을 경우 2개 이상의 위치를 모두 보여줘야 함

mynumbers = [17, 92, 18, 33, 58, 7, 33, 42, 18]
names = ["Justin", "Robert", "Anna", "Taylor"]


def solution(numbers, findNumber):
    result = []
    for i in range(0, len(numbers)):
        if numbers[i] == findNumber:
            result.append(i)
    return result


print(solution(mynumbers, 182))

# 학생번호, 이름이 리스트로 주어졌을때, 번호를 부르면 해당 인덱스에 있는
# 이름이 출력되는 함수를 만드시오. 해당 번호의 학생이 없으면 ? 를 출력하시오


def solution2(numbers, names, number):
    for i in range(0, len(numbers)):
        if numbers[i] == number:
            if i >= len(names):
                return "?"
            else:
                return names[i]


print(solution2(mynumbers, names, 58))

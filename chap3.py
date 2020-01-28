# 배열내 동명이인을 찾고, 있다면 해당 이름을 별도의 집합으로 출력하시오

names = ["Tom", "Jerry", "Mike", "Tom"]


def findName(names):
    n = len(names)
    answer = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if names[j] == names[i]:
                answer.add(names[i])
    return answer


# n명중 두명을 뽑아 짝을 지을때, 가능한 모든 조합을 출력하시오
pair = ["Tom", "Jerry", "Mike"]


def pairName(names):
    n = len(names)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print("짝 : {}-{}".format(names[i], names[j]))


pairName(pair)

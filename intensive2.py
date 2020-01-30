# 동전 문게를 재서 가짜 동전을 찾는 알고리즘


def weigh(a, b, c, d):
    fake = 29  # 가짜 동전의 테스트용 위치
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

# weigh 함수를 호출해 가짜 동전의 위치를 찾는 추가 함수


def find_fakecoin(left, right):
    for i in range(left+1, right+1):
        # 가짜 왼쪽 동전을 함수를 이용해 비교
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i
    return -1

# weigh 함수를 호출해 가짜 동전의 위치를 찾는 추가 함수


def find_fakecoin2(left, right):
    if left == right:
        return left
    hlaf = (right - left+1) // 2
    g1_left = left
    g1_right = g1_left + hlaf - 1
    g2_left = left + hlaf
    g2_right = g2_left + hlaf - 1

    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == -1:
        return find_fakecoin2(g1_left, g1_right)
    elif result == 1:
        return find_fakecoin2(g2_left, g2_right)
    else:
        return right


n = 100

print(find_fakecoin(0, n-1))
print(find_fakecoin2(0, n-1))

# 함수 실행속도 비교를 위한 알고리즘
import time
import random

# 일자별 주식 가격을 입력 받았을때 최대 수익을 냈을때의 수익을 출력하는 함수
stocks = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
# 이중 for문으로 배열내 모든 요소를 검사해서 구현 한경우 : O^2의 계산복잡도를 가짐


def find_maxprofit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n-1):
        for j in range(1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit
# for문 하나로 구현한 경우 : O(n)의 계산 복잡도를 가짐


def find_maxprofit2(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit
# 두가지 함수의 실행속도 비교를 위한 함수


def speed_test(n):
    stock = []
    for i in range(0, n):
        stock.append(random.randint(5000, 20000))
    start = time.time()
    slow_function = find_maxprofit(stock)
    end = time.time()
    slow_result = end - start
    start = time.time()
    fast_function = find_maxprofit2(stock)
    end = time.time()
    fast_result = end - start

    print("{}개의  최대 수익 : (느린 함수 실행 결과 :{}) (빠른 함수 실행 결과 :{})".format(
        n, slow_function, fast_function))
    multiplier = 0  # 느린 함수 대비 빠른 함수가 몇배 빠른지 표시하는 변수
    if fast_function > 0:
        multiplier = slow_result // fast_result
    print("%d개 값 비교시 (느린 함수 실행 시간 :%.5f) (빠른 함수 실행 시간 :%.5f), %.2f배 빠름" %
          (n, slow_result, fast_result, multiplier))


speed_test(100)

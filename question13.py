# 회문 찾기


def palindrome(s):
    queue = []
    stack = []

    for x in s:
        if x.isalpha():
            queue.append(x.lower())
            stack.append(x.lower())
    while queue:
        if queue.pop(0) != stack.pop():
            return False
    return True


print(palindrome("madam, i'm adam"))


def palindrome2(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start].isalpha() == False:
            start += 1
        elif s[end].isalpha() == False:
            end -= 1
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    return True


print("실행 결과 : ", palindrome2("madam, i'm adam"))

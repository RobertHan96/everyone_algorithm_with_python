# 그래프 문제1 : 자신의 친구, 친구의 친구를 모두 출력


def find_all_friends(friends, start):
    queue = []  # 앞으로 처리해야할 친구들의 이름 저장
    done = set()  # 큐에 추가 완료한 사람들을 체크하기 위한 집합 (중복 방지를 위해 집합으로 생성)
    queue.append(start)
    done.add(start)

    while queue:
        person = queue.pop(0)  # 친구 한명을 꺼내서 출력
        print(person)
        for x in friends[person]:  # 꺼낸 친구의 리스트를 순회하기
            if x not in done:
                queue.append(x)
                done.add(x)


myFriends = {
    'Summer': ["John", "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["John", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]
}

# 그래프 문제2 : 자신의 모든 친구를 출력하고, 친밀도까지 출력하기 (자기자신은0, 이후로 1씩 추가)


def find_all_relative(friends, start):
    queue = []  # 앞으로 처리해야할 친구들의 이름 저장
    done = set()  # 큐에 추가 완료한 사람들을 체크하기 위한 집합 (중복 방지를 위해 집합으로 생성)
    queue.append((start, 0))
    done.add(start)

    while queue:
        (person, relativity) = queue.pop(0)  # 친구 한명을 꺼내서 출력
        print(person, "-", relativity, "촌")
        for x in friends[person]:  # 꺼낸 친구의 리스트를 순회하기
            if x not in done:
                queue.append((x, relativity+1))
                done.add(x)


myTree = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}
# 그래프 문제3 : 숫자 순서도를 입력 받아 시작점부터 모든 하위 요소를 탐색해서 출력하기


def find_tree(tree, start):
    queue = []
    done = set()
    queue.append(start)
    done.add(start)

    while tree:
        num = queue.pop(0)
        print(num)
        for x in tree[num]:
            if x not in done:
                queue.append(x)
                done.add(x)


find_tree(myTree, 1)

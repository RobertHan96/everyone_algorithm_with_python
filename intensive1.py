# 미로 찾기 문제 : 딕셔너리 형태의 미로, 출발점, 도착점이 주어졌을때
# 이동 경로를 표시하고, 벽에 막혀서 나갈수 없는 미로일 경우 ?를 출력
myMaze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}


def find_road(maze, start, end):
    queue = []
    done = set()
    queue.append(start)
    done.add(start)

    while queue:
        point = queue.pop(0)
        # 입력된 딕셔너리의 값 리스트 중 마지막 값이 다음 경로이므로 -1로 마지막 요소를 불러옴
        v = point[-1]
        if v == end:
            return point  # 마지막 요소가 end point와 같으면 미로가 끝난 것이므로 반복문 종료
        for x in maze[v]:  # 미로의 끝이 아니라면 해당 요소의 리스트를 돌면서 전체 검사
            if x not in done:
                # 아직 done리스트에 없는 좌표 값은 queue와 done에 모두 추가
                queue.append(point+x)  # 이동 경로도 기억해야하므로 함께 저장
                done.add(x)
                print("해당 경로로 진행 불가 : ", point)
                print("해당 경로로 진행 불가 : ", queue)
                print("해당 경로로 진행 불가 : ", done)
    return "?"


print(find_road(myMaze, 'a', 'b'))

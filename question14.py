# 딕셔너리 활용 문제
# 학생 번호 : 이름 형태의 딕셔너리가 입력됐을때 번호에 해당하는 이름을 돌려주는 함수를 만드시오
# 해당 출석번호가 없으면 ?를 리턴하시오


myClass = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}


def check_students(students, num):
    for name in students:
        if name == num:
            return students[name]
    return "?"


print("이름 : ", check_students(myClass, 1055))

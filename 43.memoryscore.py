# 출처 :  https://school.programmers.co.kr/learn/courses/30/lessons/176963/solution_groups?language=python3&type=my


def solution(name, yearning, photo):
    dict = {i:j for i,j in zip(name,yearning)}
    answer = []
    for p in photo:
        a = 0
        for i in p:
            try:
                a+=dict[i]
            except:
                pass
        answer.append(a)
    return answer
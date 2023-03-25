# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    s0, s1 = '수', '박'
    answer = ''
    for i in range(n):
        if i%2 ==0:
            answer+=s0
        else:
            answer+=s1
    return answer
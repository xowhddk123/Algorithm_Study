# https://school.programmers.co.kr/learn/courses/30/lessons/161989?language=python3

def solution(n, m, section):
    x, answer = section[0]-1, 0
    for v in section:
        if x < v:
            x = v+m-1
            answer += 1
    return answer
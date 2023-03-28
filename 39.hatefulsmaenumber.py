# 출처 :  https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    pre = -1
    for i in arr:
        if i != pre:
            answer.append(i)
            pre = i
    return answer
# 출처 :  https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    x0=str(x)
    x1 = [int(i) for i in x0]
    if x%sum(x1)==0:
        answer=True
    else:
        answer=False
    return answer
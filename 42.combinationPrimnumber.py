# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=python3

'''
이전에 풀었던 삼총사 문제를 응용해서 풀어봤다. 
for문을 5개나 쓴건 정말 손이 떨렸지만 
도저히 다른 방법은 생각이 나지 않았다.

시간을 줄일 수 있는 다른 아이디어는 있을지 모르나 소수를 찾는것도 조합을 찾는것도 모두 완전탐색이 아니고서는 생각이 나지 않는다.
'''

def primnumber(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True

def solution(number):
    p = []
    for i in range(6,max(number)*3):
        if primnumber(i):
            p.append(i)
    answer = 0
    for n1,i in enumerate(number[:-2]):  
        for n2, j in enumerate(number[n1+1:-1],n1+1):
            for k in number[n2+1:]:
                if i+j+k in p:
                    answer+=1

    return answer
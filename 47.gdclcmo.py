# 출처 :  https://school.programmers.co.kr/learn/courses/30/lessons/12940

'''
먼저 input으로 받는 n,m의 크기를 내림차순으로 정렬해준다. 

1. 최소공배수 구하는 법
    - 큰수를 상수배하면서 작은수로 나눠질때 까지 반복문을 돌림

2. 최대공약수 구하는법
    - 작은수 부터 1까지 역순으로 돌면서 n,m이 모두 나눠지면 반복문을 멈춘다.
'''

def solution(n, m):
    if n < m:
        n, m = m, n
    i = 1
    # 최소 공배수 구하기
    while n*i%m!=0:
        i+=1
    lcm = n*i
    for j in range(m,0,-1):
        if (n%j==0)&(m%j==0):
            break
    gcd = j
    answer = [gcd, lcm]
    return answer
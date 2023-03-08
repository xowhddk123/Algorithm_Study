# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3

def solution(n):
    lst = [i for i in range(1,n+1) if n%i==0] 
    answer = sum(lst)
    return answer



# 인상깊은 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
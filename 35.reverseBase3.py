#출처 : https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    i = 0
    third = []
    # 3진법으로 바꾸기
    while n != 0:
        third.append(n % 3)
        n = n//3
        i +=1
    third.reverse()
    answer = sum([(3**i)*j for i,j in enumerate(third)])
    return answer
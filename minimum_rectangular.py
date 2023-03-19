# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

# 나의 풀이
def solution(sizes):
    sizes = [sorted(i) for i in sizes]  # 정렬
    w = max([i[1] for i in sizes])  # 가로만 정렬해서 최댓값
    h = max([i[0] for i in sizes])   # 세로만 정렬해서 최댓값
    answers = w*h
    return answers

# 깔끔한 풀이
def solution(sizes):
    row = 0
    col = 0
    for a,b in sizes:
        if a < b:           # 가로 세로 정렬
            a,b = b,a  
        row = max(row, a)   # 비교해서 계속 큰 값으로 변경
        col = max(col, b)
    answers = row*col       # 최종적으로 나온 가로세로값 곱해서 넓이
    return answers    
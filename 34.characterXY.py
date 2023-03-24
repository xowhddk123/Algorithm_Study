# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120861?language=python3

def solution(keyinput, board):
    answer = [0,0]
    row = board[0]//2  # 가로 길이
    col = board[1]//2  # 세로 길이
    dict = {'left':[-1,0], 'right':[1,0], 'up':[0,1], 'down':[0,-1]}
    for i in keyinput:
        answer[0] += dict[i][0]
        answer[1] += dict[i][1]
        if row < answer[0]:
            answer[0] -=1
        if -row > answer[0]:
            answer[0]+=1
        if col < answer[1]:
            answer[1] -=1
        if -col > answer[1]:
            answer[1] +=1
    return answer


# 좋은 풀이

def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]  # 이동 값을 먼저 받아서 
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:  # 계산을 해보고 
            continue  # 한계를 넘어가면 넘어가고
        else:
            x,y = x+dx,y+dy  # 아니면 더해서 결과 변경

    return [x,y]

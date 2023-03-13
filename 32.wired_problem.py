# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/12930

'''
1. 문자열을 받아서 split해 단어별로 쪼갠다
2. 각 단어를 for문을 돌려서 하나씩 출력
3. 짝수면 대문자, 홀수면 소문자로 빈문자열 answer에다 더한다. 
4. 한 단어가 끝나면 띄어쓰기를 해준다.
5. 마지막 단어 이후에 무의미한 띄어쓰기가 생기므로 마지만 문자는 포함하지 않는다. 
'''


def solution(x):
    answer = ''
    sentence = x.split(' ',-1)  # 빈 문자열도 문자열로 인식. (기댓값, 인자값)
    for s in sentence:
        for i, j in enumerate(s):
            if i%2==0:
                answer += j.upper()
            else:
                answer += j.lower()
        answer += ' '
    return answer[:-1]
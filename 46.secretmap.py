# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/17681

''' 
두 지도의 2진수 길이가 같다는 점에 착안해 for문은 한 번만 돌린다.
나머지 순서대로 문자열에 더해준 다음에 조건문을 통해 '#'과 ' ' 공백으로 변환해준다. 
변환된 문자를 문자열 s에 더한다. 
2진수를 구하기 위한 나머지는 뒤에서 부터 출렸되었기 떄문에 역으로 출력해서 리스트에 더한다. 
'''

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        mok1, mok2 = i,j
        s = ''
        for _ in range(n):
            mok1, na1 = divmod(mok1,2)
            mok2, na2 = divmod(mok2,2)
            na = na1+na2
            if na >=1:
                na = '#'
            else:
                na = ' '
            s+=na
        
        answer.append(s[::-1])
    return answer
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131705
'''
combination 모듈을 사용해서 풀수도 있음. 
핵심은 배열을 겹치지 않게 계속 뽑는 것
[0,1,2,3,4]의 리스트에서 
1번으로 뽑히는 것의 경우의 수는 [0,1,2]까지이다. 
왜냐하면 3,4는 2번 3번 배열에서 뽑힐것이기 떄문에 중복을 허용하지 않는 경우에서는 불가능하다. 
즉 배열은
[0,1,2]
[1,2,3]
[2,3,4]

ex)
1.[0] 
2.[1], [2], [3] 
3.[2,3,4], [3,4],[4]
이런식의 조합이 생겨난다. 
'''

def solution(number):
    answer = 0
    for n1,i in enumerate(number[:-2]):  
        for n2, j in enumerate(number[n1+1:-1],n1+1):
            for k in number[n2+1:]:
                if i+j+k==0:
                    print(i,j,k)
                    answer+=1
    return answer
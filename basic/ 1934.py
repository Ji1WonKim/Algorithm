'''
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

출력
첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
'''

t = int(input())

for i in range(t):
    aa = list(map(int,input().split()))
    a = aa[0]
    b = aa[1]
    print(a)
    while(a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    g=a
    ma = aa[0]/g
    mb = aa[1]/g

    print(g*ma*mb)

'''
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
if  중요도가 높은 문서가 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
else 그렇지 않다면 바로 인쇄를 한다.

Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 

입력
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

출력
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
'''
from collections import deque

count = 1

t = int(input())

for i in range(t):
    nn = list(map(int,input().split()))
    n = nn[0]
    ord=nn[1]
    imp = deque(map(int,input().split()))
    print(imp)
    imp_ord=imp[ord]
    while(n>0):
        if ord==0:
            if max(imp)==imp[0]:
                print(11111111111111+count)
                n = 0
        else:
            if max(imp)==imp[0]:
                imp.popleft()
                print(imp)
                count = count + 1
                ord -= 1
                n -= 1
            else: 
                imp.append(imp[0])
                imp.popleft()
                print(imp)

#내가 제일 크면 그때 count 출력





    
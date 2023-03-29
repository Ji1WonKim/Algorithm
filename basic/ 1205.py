

n, ts, p=map(int,input().split())
#n은 개수, ts는 태수 점수, p는 랭킹에 올라가는 수 10<=p<=50, 0<=n<=p

if (n == 0):
    a=1
        
else:
    list1=[]
    list1=input().split()
    list1=list(map(int, list1))
    #입력 다 받음
    minn=min(list1)
    #n==p이면서 랭킹최소값이 ts보다 클 때 -1 출력해야 함
    if ((n==p) and (minn>=ts)):
         a=-1
    else:     
        #아닐 경우만 다음 진행   
        list1.append(ts)
        list1.sort(reverse=True)
        #ts가 몇 번째인지 확인 
        a = list1.index(ts)+1


print(a)

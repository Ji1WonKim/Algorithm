import sys
from collections import deque

n = sys.stdin.readline()
que = deque()
cmd = ['push', 'pop', 'size', 'empty', 'front']


for i in range(n):
    com = sys.stdin.readline().split()
  
    if com[0]==cmd[0]:       #push
        que.append(int(com[1]))
      
    elif com[0]==cmd[1]:      #pop
        if len(que)>0:
          print(que[0])
          que.popleft()
        else:
          print(-1)
    
    elif com[0]==cmd[2]:           #size
        print(len(que))
      
    elif com[0]==cmd[3]:          #empty
        if len(que)==0:
          print(1)
        else:
          print(0)
        
    elif com[0]==cmd[4]:         #front
        if len(que)>0:
          print(que[0])
        else:
          print(-1)
    
    else:                           #back
        if len(que)>0:
            print(que[-1])
        else:
            print(-1)
      
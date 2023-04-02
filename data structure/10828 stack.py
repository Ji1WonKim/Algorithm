import sys
n = int(input())
stack = []
cmd = ['push', 'pop', 'size', 'empty']


for i in range(n):
    com = sys.stdin.readline().split()
  
    if com[0]==cmd[0]:       #push
        stack.append(int(com[1]))
      
    elif com[0]==cmd[1]:      #pop
        if len(stack)>0:
          print(stack[-1])
          stack.pop()
        else:
          print(-1)
    
    elif com[0]==cmd[2]:           #size
      print(len(stack))
      
    elif com[0]==cmd[3]:          #empty
        if len(stack)==0:
          print(1)
        else:
          print(0)
        
    else:                             #top
        if len(stack)>0:
          print(stack[-1])
        else:
          print(-1)

  

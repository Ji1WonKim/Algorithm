

sik = input()
sik = sik.replace('-', '.-.')
sik = sik.replace('+', '.+.')
sik = sik.split('.')
ans = 0
count = 0

#-가 나오기 전까지 다 더함
for i in range(len(sik)):
    if (sik[i]!='-'):
        if (sik[i]!='+'):
            ans = ans + int(sik[i])
            count += 1
    else:
        break


remove = {'-', '+'}
sik = [i for i in sik if i not in remove]

len1 = len(sik)

for i in range(count, len1):
    for j in sik[i].split('+'):
        ans = ans - int(j)

print(ans)


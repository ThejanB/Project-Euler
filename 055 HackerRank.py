non_lychrel={}
n=int(input().strip())
for i in range(10,n):
    j=0
    t=i
    while j<60 and str(t)!=str(t)[::-1]:
        t=t+int(str(t)[::-1])
        j+=1
    if str(t)==str(t)[::-1]:
        non_lychrel[t]=non_lychrel[t]+1 if t in non_lychrel else 1
m=max(non_lychrel,key=non_lychrel.get)
print(m,non_lychrel[m])
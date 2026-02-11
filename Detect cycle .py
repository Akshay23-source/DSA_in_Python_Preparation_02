a=[1,2,3,4]; slow=fast=0
while fast<len(a)-1:
    slow+=1; fast+=2
    if slow==fast: print("Cycle"); break
else: print("No Cycle")


a=[1,2,3,2]
s=set()
for x in a:
    if x in s:print("Cycle");break
    s.add(x)
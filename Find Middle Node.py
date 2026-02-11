a=[1,2,3,2,4,4,5]
slow=fast=0
while fast<len(a)-1: slow+=1;fast+=2
print(a[slow])



a=[1,2,3,4,5,6,7,8,9]
print(a[len(a)//2])
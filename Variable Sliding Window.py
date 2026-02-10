a=[2,1,5,2,3]; t=7
l=s=m=0
for r in range(len(a)):
    s+=a[r]
    while s>t: s-=a[l]; l+=1
    m=max(m,r-l+1)
print(m)




a=[1,2,1,1]; t=3
l=s=m=0
for r in range(len(a)):
    s+=a[r]
    while s>t: s-=a[l]; l+=1
    m=max(m,r-l+1)
print(m)

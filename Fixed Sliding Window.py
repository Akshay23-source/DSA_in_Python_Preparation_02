a=[2,3,1,1,4,3,2,];k=3
s=sum(a[:k]);m=s
for i in range(k,len(a)):
    s+=a[i]-a[i-k]; m=max(m,s)
    print(m)
    
    
    
a=[1,2,3,4]; k=2
s=sum(a[:k])
for i in range(k,len(a)): s=max(s,sum(a[i-k+1:i+1]))
print(s)
   
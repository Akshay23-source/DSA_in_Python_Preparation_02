a=[1,2,2,2,3]; t=2; ans=-1
l,r=0,len(a)-1
while l<=r:
    m=(l+r)//2
    if a[m]>=t: r=m-1
    else: l=m+1
    if a[m]==t: ans=m
print(ans)







a=[1,2,2,2,3]; t=2; ans=-1
l,r=0,len(a)-1
while l<=r:
    m=(l+r)//2
    if a[m]<=t: l=m+1
    else: r=m-1
    if a[m]==t: ans=m
print(ans)

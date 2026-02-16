a=[1,3,5,7,9]; t=7
l,r=0,len(a)-1
while l<=r:
    m=(l+r)//2
    if a[m]==t: print(m); break
    elif a[m]<t: l=m+1
    else: r=m-1





a=[2,4,6,8]; t=6
l,r=0,len(a)-1
while l<=r:
    m=(l+r)//2
    if a[m]==t: print(True); break
    elif a[m]<t: l=m+1
    else: r=m-1

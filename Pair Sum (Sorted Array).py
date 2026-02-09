a=[1,2,4,7]; t=9
l,r=0,len(a)-1
while l<r:
    if a[l]+a[r]==t: print(True); break
    elif a[l]+a[r]<t: l+=1
    else: r-=1




a=[1,3,5,7]; t=8
l,r=0,len(a)-1
while l<r:
    if a[l]+a[r]==t: print(l,r); break
    elif a[l]+a[r]<t: l+=1
    else: r-=1

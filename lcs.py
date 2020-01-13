# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:43:05 2019

@author: B.Mounika
"""
import numpy as np
n=int(input())
z=np.array(list(map(int,input().split())))
assert (n,)==z.shape, exit(1)
assert n<=3*(10**5), exit(1)
assert np.sum(z>1000000000)+np.sum(-1000000000>z)==0, exit(1)
s=np.cumsum(z)
print(s)
mint=0
ans=(0,0)
for el in s:
    tup=(el-mint,1)
    ans=max(ans,tup)
    print(ans)
    mint=min(mint,el)
    print(mint)
if ans == (0,1):
    ans=(0,np.sum(z==0))
else:
    aim,dum=ans
    cnt=0
    mint=0
    for el in s:
        if aim == el-mint:
            cnt+=1
            mint=el
        mint=min(mint,el)
    ans=(aim,cnt)
print(str(ans[0])+" "+str(ans[1]))
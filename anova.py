import pandas as pd
import scipy.stats
import numpy as np
import math
n=int(input("enter no.of treatments:"))
tr=[]
for i in range(n):
    t=list(map(float,input("enter x vales:").split()))
    tr.append(t)
print(tr)
G=0
ssr=0

nt=0
ti2=0
for i in tr:
    t=0
    ni=0
    for j in i:
       
        ni=ni+1
        G=G+j;
        t=t+j
        ssr=ssr+j**2

    nt=nt+ni
    ti2+=(t**2)/ni  

print("G:",G)

CF=(G**2)/(nt)

sst=ssr-CF

sstr=ti2-CF

sse=sst-sstr


print("ssr:",ssr)
print("CF:",CF)
print("sst:",sst)
print("sstr",sstr)
print("sse:",sse)

dt=n-1
de=nt-n
dt=nt-1

msstr=sstr/dt
print("MSSTR:",msstr)
msse=sse/de

print("MSSE:",msse)


alpha=float(input("enter alpha value:"))

f=msstr/msse

if(f>1):
    f=msstr/msse
    f_tab=scipy.stats.f.ppf(1-alpha,dt,de)
elif(f<1):
    f=msse/msstr
    f_tab=scipy.stats.f.ppf(1-alpha,de,dt)
print("F calculated value is:",f)
print("F table value is:",f_tab)

if(f>f_tab):
    print("reject null hypothesis")
else:
          print("accept null hypothesis")




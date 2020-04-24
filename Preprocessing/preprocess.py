# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:10:26 2019

@author: sanja
"""

import pandas as pd 
# reading csv file  
data=pd.read_csv("reqdata_edit.csv") 
reqdata=data[['TIMESTAMP','POLYLINE']]
df=pd.DataFrame(reqdata)
poly=data[['POLYLINE']]
df = pd.DataFrame(poly)
sources=[]
for i in data['POLYLINE']:
  sources.append(i)
"""for i in range(len(sources)):
    sources[i]=sources[i].replace(']','')
    sources[i]=sources[i].replace('[','')
df=pd.DataFrame(poly)"""


dff = pd.DataFrame() 
l1=[]
l2=[]
for j in range(len(sources)-1):
    s=sources[j].split(',')
    d1=s[-2].replace('[','')
    d1=d1.replace(']','')
    d2=s[-1].replace('[','')
    d2=d2.replace(']','')
    d1=float(d1)
    d2=float(d2)    
    l1.append(d1)
    l2.append(d2)
    #print(l1[j])
    #print(l2[j])
dff = pd.DataFrame(list(zip(l1, l2)), 
               columns =['P1', 'P2']) 
dff.to_csv('rdatasd.csv',index=False) 
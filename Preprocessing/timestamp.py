# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:16:39 2019

@author: sanja
"""
from datetime import datetime
import pandas as pd
data = pd.read_csv("cab_rides.csv")
dates=[]
for i in data['time_stamp']:
  i=i/1000
  dt_object = datetime.fromtimestamp(i)
  only_date=dt_object.date().strftime("%m/%d/%Y")
  dates.append(only_date)
sources=[]
for i in data['source']:
  sources.append(i)
m={}
for i in range(len(dates)):
  m[(dates[i],sources[i])]=0
for i in range(len(dates)):
  m[(dates[i],sources[i])]+=1
for i in m:
  print(i[0],i[1],m[i])
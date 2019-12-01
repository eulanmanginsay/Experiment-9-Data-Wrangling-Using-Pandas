import pandas as pd
a={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
Math=pd.DataFrame(a,columns=['Student','Math'])
b={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
Electronics=pd.DataFrame(b,columns=['Student','Electronics'])
c={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
Geas=pd.DataFrame(c,columns=['Student','GEAS'])
d={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
Esat=pd.DataFrame(d,columns=['Student','ESAT'])

merge1=pd.merge(Math, Electronics,how='outer', on='Student')
merge2=pd.merge(Geas, Esat,how='outer', on='Student')
merge=pd.merge(merge1,merge2, how='outer',on='Student')

melted1=pd.melt(merge, id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
finalMelt=melted1.rename(columns={'variable':'Subject','value':'Grades'})
x= finalMelt.sort_values('Student')
y= x.reset_index()
z=y.drop(columns='index')
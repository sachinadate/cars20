import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor as RFR


import os
dirspot = os.getcwd()
print(dirspot)

url=dirspot+"\\car\\car_data.csv"

df = pd.read_csv(url,header=0,encoding = 'unicode_escape')
df2 = df.dropna(axis = 0)
df2.rename(columns = {'Registered City':'RegisteredCity'}, inplace = True)
not_num = df2.select_dtypes(include = ['object']).columns
df3 = df2[df2.Condition != 'New']
df3['Price'] = np.log(df3.Price)
df3 = df3.drop("Condition", axis=1)
df3 = df3.drop("Transaction Type", axis=1)
not_num = df3.select_dtypes(include = ['object']).columns
df4=df3[not_num]
lab=LabelEncoder()
df3['Brand']=lab.fit_transform(df3['Brand'].astype('str'))
df3['Fuel']=lab.fit_transform(df3['Fuel'].astype('str'))
df3['Model']=lab.fit_transform(df3['Model'].astype('str'))
df3['RegisteredCity']=lab.fit_transform(df3['RegisteredCity'].astype('str'))
X = df3.drop('Price', axis = 1)
y = df3['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#Reg = LinearRegression()
#Reg.fit(X_train, y_train)
ForestReg = RFR()
ForestReg.fit(X_train, y_train)
df5=pd.merge(df3[not_num],df4,left_index=True,right_index=True)
for x in not_num:
    df5.rename(columns = {x+'_y':x}, inplace = True) 



def fun(xin):
    
    #fun
    xarr=[]
    #xin=['Toyota','Diesel',1.0,'Prado','Karachi',1997.0]#input
    colu=list(X.columns)
    #xnono=pd.Series(not_num)
    for i in range(len(xin)):
        xarr.append([colu[i],xin[i]])
    xarr[0][1]=df5['Brand_x'][df5.Brand==xin[0]].iloc[0]
    xarr[1][1]=df5['Fuel_x'][df5.Fuel==xin[1]].iloc[0]
    xarr[3][1]=df5['Model_x'][df5.Model==xin[3]].iloc[0]
    xarr[4][1]=df5['RegisteredCity_x'][df5.RegisteredCity==xin[4]].iloc[0]
    xfi=pd.DataFrame([[xarr[i][1] for i in range(len(xin))]],columns=['Brand','Fuel','KMs Driven','Model','Registered City','Year'])
    yxin=ForestReg.predict(xfi)
    return (np.exp(yxin)[0])








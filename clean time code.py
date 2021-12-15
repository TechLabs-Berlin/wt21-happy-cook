import numpy as np
import pandas as pd
import re
df2=pd.read_csv("core-data_recipe.csv",skip_blank_lines=True)

#filter the ones with structured time data
df3=df2.loc[df2.cooking_directions.str.contains('Prep',na=False)]
#transform the cooking_directions into a list
df3['cooking_directions'] = df3.cooking_directions.apply(lambda x: x[1:-1].split('\\n'))
#split the time into different columns
df3["prep_time"]=df3["cooking_directions"].apply(lambda x:x[1:2])
df3["cook_time"]=df3["cooking_directions"].apply(lambda x:x[3:4])
df3["total_time"]=df3["cooking_directions"].apply(lambda x:x[5:6])
df3['prep_time']=df3['prep_time'].str[0]
df3['cook_time']=df3['cook_time'].str[0]

#clean prep_time 
##creating a subdataframe containing days
df7=df3.loc[df3.prep_time.str.contains('d',na=False)]
##creating a subdataframe containing hours
df12=df3.loc[df3.prep_time.str.contains('h',na=False)]
## to clean the times with hours
df12['prep_time_hour']=df12['prep_time'].str[0]
df12['prep_time_hour']=df12['prep_time_hour'].apply(pd.to_numeric,errors='coerce')
### convert hours into minutes
df12["prep_time_hour"]=df12['prep_time_hour'].apply(lambda x: x*60)
df12['prep_time_min']=df12["prep_time"].apply(lambda x:x[4:])
df12['prep_time_min']=df12['prep_time_min'].str.replace('m','')
df12['prep_time_min']=df12['prep_time_min'].apply(pd.to_numeric,errors='coerce')
df12['prep_time_2']=df12['prep_time_hour']+df12['prep_time_min']
###making the nan value into zero (it works as the hours and minutes are splited)
df12['prep_time_min']=df12['prep_time_min'].fillna(0)
df12['prep_time']=df12['prep_time_2']
df12=df12.drop(columns=['prep_time_min',"prep_time_hour",'prep_time_2'])
df3['prep_time2']=df12['prep_time']
df3['prep_time2']=df3['prep_time2'].fillna(0)
##clean preptime with minutes
###turn the columns into float
df3['prep_time']=df3['prep_time'].str.replace('m','')
df3['prep_time']=df3['prep_time'].apply(pd.to_numeric,errors='coerce')
df3['prep_time']=df3['prep_time'].fillna(0)
##clean preptime with days
df7["prep_time_day"]=df7["prep_time"].apply(lambda x:x[:2])
df7['prep_time_day']=df7['prep_time_day'].apply(pd.to_numeric,errors='coerce')
df7['prep_time_day']=df7['prep_time_day'].apply(lambda x: x*60*24)
df7["prep_time_min"]=df7["prep_time"].apply(lambda x:x[4:])
df7['prep_time_min']=df7['prep_time_min'].str.replace('m','')
df7['prep_time_min']=df7['prep_time_min'].apply(pd.to_numeric,errors='coerce')
df7['prep_time']=df7["prep_time_min"]+df7["prep_time_day"]
##merge the columns of both hours and minutes and only minutes and days
df3['prep_time2']=df3['prep_time2'].fillna(0)
df3['prep_time']=df3['prep_time']+df3['prep_time2']
df3['prep_time3']=df7['prep_time']
df3['prep_time3']=df3['prep_time3'].fillna(0)
df3['prep_time']=df3['prep_time2']+df3['prep_time']+df3['prep_time3']
df3=df3.drop(columns=["prep_time2",'prep_time3'])

#Clean Cook_time
#create a sub data frame that contains days
df6=df3.loc[df3.cook_time.str.contains('d',na=False)]
#create a sub data frame that contains hours
df4=df3.loc[df3.cook_time.str.contains('h',na=False)]
##cleaning cooking time with only minutes
df3["cook_time3"]=df3['cook_time'].str.replace('m','')
df3['cook_time3']=df3['cook_time3'].apply(pd.to_numeric,errors='coerce')
df3['cook_time3']=df3['cook_time3'].fillna(0)
##cleaning cooking time with days
df6['cook_time_day']=df6["cook_time"].str[0]
df6['cook_time_day']=df6['cook_time_day'].apply(pd.to_numeric,errors='coerce')
df6['cook_time_day']=df6['cook_time_day'].apply(lambda x: x*60*24)
df6["cook_time_min"]=df6["cook_time"].apply(lambda x:x[4:])
df6["cook_time_day"]=df6["cook_time"].apply(lambda x:x[:2])
df6['cook_time_day']=df6['cook_time_day'].apply(pd.to_numeric,errors='coerce')
df6['cook_time_day']=df6['cook_time_day'].apply(lambda x: x*60*24)
df6['cook_time_min']=df6['cook_time_min'].str.replace('m','')
df6['cook_time_min']=df6['cook_time_min'].apply(pd.to_numeric,errors='coerce')
df6['cook_time']=df6['cook_time_min']+df6['cook_time_day']
#integrated into the df3
df3["cook_time"]=df6["cook_time"]
##cleaning cook_time containing hours
df4['cook_time_hour']=df4['cook_time'].str[0]
df4['cook_time_hour']=df4['cook_time_hour'].apply(pd.to_numeric,errors='coerce')
## convert hours into minutes
df4["cook_time_hour"]=df4['cook_time_hour'].apply(lambda x: x*60)
##spilt the minutes and turn minutes into float
df4['cook_time_min']=df4["cook_time"].apply(lambda x:x[4:])
df4['cook_time_min']=df4['cook_time_min'].str.replace('m','')
df4['cook_time_min']=df4['cook_time_min'].apply(pd.to_numeric,errors='coerce')
##making the nan value into zero (it works as the hours and minutes are splited)
df4['cook_time_min']=df4['cook_time_min'].fillna(0)
##getting the cook_time
df4['cook_time_2']=df4['cook_time_hour']+df4['cook_time_min']
df3['cook_time2']=df4['cook_time_2']
df3['cook_time2']=df3['cook_time2'].fillna(0)
df3['cook_time']=df3['cook_time'].fillna(0)
df3['cook_time']=df3['cook_time2']+df3["cook_time"]+df3['cook_time3']
#cleaning the dataset
df3=df3.drop(columns=['cook_time3','cook_time2'])

#getting the total cooking time
df3['total_time']=df3['prep_time']+df3['cook_time']
df3

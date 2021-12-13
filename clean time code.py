#code to clean time columns created by Ganyi
import numpy as np
import pandas as pd
import re
df=pd.read_csv("core-data-test_rating.csv")
df2=pd.read_csv("core-data_recipe.csv")
#filter out the rows with mising values
df3=df2.loc[df2.cooking_directions.str.contains('Prep',na=False)]

#transform the cooking_directions into a list
df3['cooking_directions'] = df3.cooking_directions.apply(lambda x: x[1:-1].split('\\n'))
#split the time into different columns
df3["prep_time"]=df3["cooking_directions"].apply(lambda x:x[1:2])
df3["cook_time"]=df3["cooking_directions"].apply(lambda x:x[3:4])
df3["total_time"]=df3["cooking_directions"].apply(lambda x:x[5:6])
df3['prep_time']=df3['prep_time'].str[0]
df3['cook_time']=df3['cook_time'].str[0]
#turn the columns into float
df3['prep_time']=df3['prep_time'].apply(pd.to_numeric,errors='coerce')

#create a sub data frame that contains hours
df4=df3.loc[df3.cook_time.str.contains('h',na=False)]
df4['cook_time_hour']=df4['cook_time'].str[0]
df4['cook_time_hour']=df4['cook_time_hour'].apply(pd.to_numeric,errors='coerce')
df4
# convert hours into minutes
df4["cook_time_hour"]=df4['cook_time_hour'].apply(lambda x: x*60)
#spilt the minutes and turn minutes into float
df4['cook_time_min']=df4["cook_time"].apply(lambda x:x[4:])
df4['cook_time_min']=df4['cook_time_min'].str.replace('m','')
df4['cook_time_min']=df4['cook_time_min'].apply(pd.to_numeric,errors='coerce')
#making the nan value into zero (it works as the hours and minutes are splited)
df4['cook_time_min']=df4['cook_time_min'].fillna(0)
#getting the cook_time
df4['cook_time_2']=df4['cook_time_hour']+df4['cook_time_min']
df3['cook_time']=df3['cook_time'].fillna(0)
df3['cook_time2']=df4['cook_time_2']
df3['cook_time2']=df3['cook_time2'].fillna(0)
df3['cook_time']=df3['cook_time']+df3['cook_time2']
df3=df3.drop(columns='cook_time2')
#getting prep_time
df3['prep_time']=df3['prep_time'].str.replace('m','')
df3['prep_time']=df3['prep_time'].apply(pd.to_numeric,errors='coerce')
#getting total cook time
df3['total_time']=df3['prep_time']+df3['cook_time']

#integrated the columns back to the main data frame
df2["cook_time"]=df3['cook_time']
df2["total_time"]=df3["total_time"]
df2["prep_time"]=df3['prep_time']
df2


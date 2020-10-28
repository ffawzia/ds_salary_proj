# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:46:37 2020

@author: ffawz
"""

import pandas as pd

df= pd.read_csv('glassdoor_jobs.csv')

#salary parsing

df['employer_provided']=df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)
df['per hour']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
salary=df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd=salary.apply(lambda x: x.replace('K','').replace('$',''))
minus_hr=minus_kd.apply(lambda x: x.lower().replace('employer provided salary:','').replace('per hour',''))
df['Min Salary']=minus_hr.apply(lambda x: int(x.split('-')[0]))
df['Max Salary']=minus_hr.apply(lambda x: int(x.split('-')[1]))
df['Average']=(df['Min Salary']+df['Max Salary'])/2

#company name text only
df['Company Text']=df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'] [:-3], axis=1)

#state field
df['State']=df['Location'].apply(lambda x: x.split(', ')[1])
df['State'].value_counts()

#age of company
df['Age']=df['Founded'].apply(lambda x: x if x<0 else 2020 - x)

#job description parsing 
#python
df['Python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.Python.value_counts()

#R studio
df['R studio']=df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['R studio'].value_counts()

#spark
df['Spark']=df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.Spark.value_counts()

#aws
df['aws']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws'].value_counts()

#excel
df['excel']=df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel'].value_counts()
df.columns

df_out=df.drop({'Headquarters'}, axis=1).drop(['Competitors'])
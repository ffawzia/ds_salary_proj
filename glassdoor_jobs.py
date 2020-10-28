# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 00:14:26 2020

@author: ffawz
"""

import glassdoor_scraper as gs
import pandas as pd
path= 'C:/Users/ffawz/Documents/ds_salary_proj/chromedriver'
df = gs.get_jobs('Data Scientist',1000, False, path, 15)
df.to_csv('glassdoor_jobs.csv',index=False)

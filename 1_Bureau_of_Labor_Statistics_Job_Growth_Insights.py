#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install --upgrade certifi')
get_ipython().system('pip install pandas openpyxl')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')
get_ipython().system('pip install numpy')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
from bs4 import BeautifulSoup
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


'''Read Excel Data from Bureau of Labor Statistics Workbook, Table 1.3 Fastest growing occupations, 2025 and projected 2035'''
file_path = '/home/9305ec59-5b1c-43a9-af36-3ed182cbf122/anaconda_projects/41332797-06ec-4da5-b771-68c54bd6009c/BLS_Statistics_8_27_2026.xlsx'
ep_df = pd.read_excel(file_path, sheet_name='Table 1.3',header=[1])
print('\nData obtained from https://www.bls.gov/emp/tables/fastest-growing-occupations.htm; US Bureau of Labor Statistics: Table 1.3 Fastest growing occupations, 2025 and projected 2035 (Employment in thousands)\n')
ep_df.head()


# In[4]:


'''Create dataframe object that doesn't include the total of all occupations.'''
occupations = ep_df[1:31]
'''Bar chart showcasing total jobs in 2025 and projected job totals in 2035''' 
bar_2025_2035 = occupations.plot(kind='bar',
                            x='2025 National Employment Matrix title',
                            y=['Employment, 2025','Employment, 2035'],
                            title='Total Jobs for Fast Growing Occupations in 2025 and Projected for 2035',
                            xlabel='Occupations',
                            ylabel='Total Jobs in Thousands',
                            figsize=(15,5)
                           )
print('\nOf all the fastest growing occupations in 2025, home health and personal care aides account for the most jobs and are expected to remain at the top for the next 10 years. Computer & information systems managers and medical & health service managers come in second and third respectively, though the latter is projected to surpass the former by 2035.\n')


# In[5]:


'''Scatter plot showcasing total jobs where the size of the bubble corresponds to the projected growth, percentage-wise.'''
sizes = occupations.loc[:,'Employment change, percent, 2025–35']
scatter_percent = occupations.plot(kind='scatter',
                                   x='2025 National Employment Matrix title',
                                   y='Employment, 2025',
                                   s=sizes*10,
                                   alpha=0.5,
                                   c='red',
                                   title='Jobs in 2025 and Their Projected Growth Percentage',
                                   xlabel='Occupations',
                                   rot=90,
                                   ylabel='Total Jobs in 2025',
                                   figsize=(10,5)
                                  )
print('\nPercentage-wise, Nurse Practitioners, Solar Voltaic Installers, Data Scientists, and Wind Turbine Service Technicians should see the most growth in jobs.\n')


# In[6]:


'''Scatter plot showcasing job counts in 2025 and their projected growth in thousands'''
sizes_1 = occupations.loc[:,'Employment change, numeric, 2025–35']
scatter_numeric = occupations.plot(kind='scatter',
                                   x='2025 National Employment Matrix title',
                                   y='Employment, 2025',
                                   s=sizes_1,
                                   alpha=0.5,
                                   c='red',
                                   title='Jobs in 2025 and Their Projected Growth in Thousands',
                                   xlabel='Occupations',
                                   rot=90,
                                   ylabel='Total Jobs in 2025',
                                   figsize=(10,5)
                                  )
print('\nHome health & personal care aids will have the most job growth in total.\n''(Job growth denoted by size of bubble.)\n')


# In[7]:


'''Box plot showcasing median wages in 2025 for fastest growing occupations'''
wages_box = occupations.plot(kind='bar',
                       x='2025 National Employment Matrix title',
                       y='Median annual wage, dollars, 2025',
                       title='Median Annual Wage for Fastest Growing Occupations in 2025',
                       xlabel='Occupations',
                       ylabel='Wages',
                       figsize=(15,5)
                      )
'''Calculations for median wage sum of specific job categories and their comparison to the total sum of all median wages for the fastest growing occupations'''
med_wage_sum = occupations['Median annual wage, dollars, 2025'].sum()
titles = occupations['2025 National Employment Matrix title'].str.strip()

healthcare_jobs = ['Nurse practitioners','Medical and health services managers','Psychiatric technicians','Ophthalmic medical technicians','Physician assistants','Occupational health and safety technicians','Epidemiologists','Occupational health and safety specialists','Home health and personal care aides','Health specialties teachers, postsecondary','Nursing instructors and teachers, postsecondary','Health information technologists and medical registrars','Diagnostic medical sonographers']
healthcare_jobs_sum = occupations.loc[titles.isin(healthcare_jobs), 'Median annual wage, dollars, 2025'].sum()
healthcare_slice = (healthcare_jobs_sum / med_wage_sum) * 100
print('\nExcluding positions associated with therapy, jobs that fall under the umbrella of healthcare account for', f'{healthcare_slice:.2f}','% of median wages earned amongst the fastest growing occupations.\n')

computer_tech_jobs = ['Data scientists','Computer and information research scientists','Information security analysts','Computer and information systems managers']
computer_tech_jobs_sum = occupations.loc[titles.isin(computer_tech_jobs), 'Median annual wage, dollars, 2025'].sum()
computer_tech_slice = (computer_tech_jobs_sum / med_wage_sum) * 100
print('\nJobs that fall under computer science and information technology account for', f'{computer_tech_slice:.2f}','% of median wages earned.\n')



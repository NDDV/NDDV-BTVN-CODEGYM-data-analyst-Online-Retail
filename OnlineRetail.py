#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('OnlineRetail.csv')
df

#%%
df['month'] = pd.to_datetime(df['InvoiceDate'],format='%m/%d/%Y %H:%M').dt.month
df
# %%
conditions = [df['month'] == 1 , df['month'] == 2 , df['month'] == 3, \
    df['month'] == 4 , df['month'] == 5 , df['month'] == 6,\
        df['month'] == 7 , df['month'] == 8 , df['month'] == 9,\
    df['month'] == 10 , df['month'] == 11 , df['month'] == 12]
choices = ['1','1','1','2','2','2','3','3','3','4','4','4']
df['previous'] =np.select(conditions,choices)
df
# %%
df['Amount'] = df['Quantity'] * df['UnitPrice']
df
# %%
cond = [(df['Country'] == 'United Kingdom' & df['month'] == 10),\
    (df['Country'] == 'United Kingdom' & df['month'] == 11),\
        (df['Country'] == 'United Kingdom' & df['month'] == 12),\
    df['Country'] =='France']
choi = [10,10,10,5]

df['Discount'] = np.select(cond,choi,default=0)
df
#%%
df['Total'] = df['Amount'] - df['discount']
df

# %%

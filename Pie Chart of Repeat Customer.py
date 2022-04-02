#!/usr/bin/env python
# coding: utf-8

# In[136]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
#Charts
import matplotlib.pyplot as plt
import matplotlib.pyplot as figure
import numpy as np


# In[41]:


#Reading in dataset 
dataFrame= pd.read_csv("/Users/Tyler/Desktop/OCF/Market_info.csv")


# In[167]:


dataFrame


# In[ ]:


individual_order_total = ['Orders',dataFrame['Orders'].value_counts()]


# In[153]:


individual_order_total = dataFrame['Orders'].value_counts()


# In[154]:


indi_order = pd.DataFrame(individual_order_total)


# In[156]:


indi_order


# In[84]:


Single = dataFrame.loc[(dataFrame['Orders']==1)]


# In[166]:


def autopct_generator(limit):
    def inner_autopct(pct):
        return ('%.2f%%' % pct) if pct > limit else ''
    return inner_autopct

labels = ['Single Purchase','Two Time','Three Time']
sizes = indi_order['Orders']
NUM_COLORS = len(sizes)

fig1, ax1 = plt.subplots(figsize=(6, 5))

theme = plt.get_cmap('bwr')


box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 1.3, box.height])

_, _, autotexts = ax1.pie(
    sizes, autopct=autopct_generator(7), startangle=90, radius=1.8 * 1000)
for autotext in autotexts:
    autotext.set_weight('bold')
ax1.axis('equal')
total = sum(sizes)
plt.legend(loc='upper right',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 12},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure)
# fig1.set_size_inches(18.5, 10.5)
fig1.savefig('chart.png')


# In[ ]:





# In[88]:


def countOccurrences(O_list, n, x):
    res = 0
    for i in range(n):
        if x == arr[i]:
            res += 1
    return res
  
# Driver code
n = len(O_list)
x = 53
print (countOccurrences(O_list, n, x))


# In[ ]:





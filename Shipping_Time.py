#!/usr/bin/env python
# coding: utf-8

# In[121]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
#Charts
import matplotlib.pyplot as plt
import matplotlib.pyplot as figure
import numpy as np


# In[142]:


#Reading in dataset 
dataFrame= pd.read_csv("/Users/Tyler/Desktop/OCF/Packing_Speed/Order_to_Ship.csv")


# In[138]:


Items = dataFrame['Product Details'].str.split(",", expand = True)
Items = Items.drop([2,5,8,9],axis = 1)


# In[144]:


Empty ={
    'Order Date': dataFrame['Order Date'],
    'Date Shipped': dataFrame['Date Shipped'],
    'Quantity' :Items[1].str.split(":", expand = True)[1],
    'ID' :Items[0].str.split(":", expand = True)[1],
    'Product Name' :Items[3].str.split(":", expand = True)[1],
    'Weight' :Items[4].str.split(":", expand = True)[1],
    'Unit Price' :Items[6].str.split(":", expand = True)[1],
    'Total Price' :Items[7].str.split(":", expand = True)[1]
}


# In[145]:


Products_Sold = pd.DataFrame(Empty)


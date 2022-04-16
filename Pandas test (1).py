#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
df = pd.read_csv('auto.csv')


# In[ ]:


# 1. Find the most expensive car company name


# In[3]:


automobile.head()


# In[9]:


car_price = max(df['price'])
car_price


# In[11]:


expensive_car = df[df['price'] == car_price]['make'].to_string(index=False).strip()
expensive_car


# In[ ]:


# 2 Count total cars per company


# In[16]:


import pandas as pd
import numpy as np
df = pd.read_csv('auto.csv')
df['make'].value_counts()


# In[ ]:


# 3.Find each company’s highest price car


# In[19]:


import pandas as pd
import numpy as np
df = pd.read_csv('auto.csv')
highest_price = df.groupby('make')
price = highest_price['make','price'].max()
price


# In[ ]:


# 4. Sort all cars by Price column


# In[25]:


import pandas as pd
import numpy as np
df = pd.read_csv('auto.csv')
df = df.sort_values(by=['price'], ascending=False)
df.head(10)


# In[ ]:


# 5.group by make, fuel-type and body-style to calculate the average of city-mpg and highwaympg (miles per gallon)


# In[28]:


group = df.groupby(['make','fuel_type','body_style']).agg({'city_mpg': ['mean'], 'highway_mpg' : ['mean']})
group


# In[ ]:





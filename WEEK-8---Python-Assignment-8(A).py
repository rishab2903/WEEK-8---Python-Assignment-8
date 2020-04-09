#!/usr/bin/env python
# coding: utf-8

# In[9]:



import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv("~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.csv")
df.head()





ax = df.hist(column='age', by='gender', figsize=(15,6), rot=0)
ax[0].set_xlabel('Age')
ax[1].set_xlabel('Age')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





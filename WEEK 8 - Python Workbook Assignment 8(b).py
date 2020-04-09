#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]


# In[3]:


GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)
df


# In[4]:


df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df
    


# In[5]:


plt.pie(df['TotalDemerits'])


# In[6]:


plt.pie(df['TotalDemerits'],
        labels=df['Names'],
        explode=(0,0,0,0,0.05),
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[7]:


result=[]
for value in df['TotalDemerits']:
    if value <2:
        result.append(100)
    elif value < 7 and value >= 2:
        result.append(75)
    else:
        result.append(50)
       
df["Result"] = result 
df


# In[9]:


plt.pie(df['Result'],
        labels=df['Names'],
        explode=(0,0,0,0.05,0),
        startangle=90,
        autopct='%1.1f%%',)
plt.axis('equal')
plt.show()


# In[ ]:





# In[ ]:





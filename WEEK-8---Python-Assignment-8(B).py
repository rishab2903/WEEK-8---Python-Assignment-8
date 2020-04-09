#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions','Warnings']
df1 = pd.DataFrame(data = list(GradeList), columns=columns)
df1['TotalDemerits'] = df1['Absences'] + df1['Detentions'] + df1['Warnings']




plt.pie(df1['TotalDemerits'],labels=df1['Names'],explode=(0,0,0,0.15,0),startangle=180,
        autopct='%1.2f%%',shadow=True, textprops={'weight': 'bold'})
plt.axis('equal')
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





# In[ ]:





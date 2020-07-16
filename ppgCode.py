#!/usr/bin/env python
# coding: utf-8

# In[52]:


import os
import pandas as pd



# In[116]:


"""
This function helps execute a structed walk within the directory specified by PATH, 
grab data pertaining to the device DEVICE_NAME
and form a pandas dataframe
"""

#Key variables 
PATH="/Users/momamouei/Documents/Projects/My_daily_Physio/daily_recordings"
DEVICE_NAME="A02362"

#Go to sub-directory and check the number of days
days_dirs=[PATH+"/"+i for i in filter(lambda x: os.path.isdir(PATH+"/"+x),os.listdir(PATH))]
print("Found {0} days of recording".format(len(days_dirs)))

#Go to each day and see different sessions
day_dir=days_dirs[0]
recording_sessions=list(filter(lambda x:(os.path.isdir(day_dir+"/"+x) and (x[-6:]==DEVICE_NAME)),os.listdir(day_dir)))

print("Found {0} recordings for device {1} in day {2}".format(len(recording_sessions),DEVICE_NAME,day_dir[-10:]))

recording_session_dirs=[day_dir+"/"+recording_session for recording_session in recording_sessions]

#Read the data for each session
for recording_session_dir in recording_session_dirs:
    for file in os.listdir(recording_session_dir):
        print(file)  
    
    


# In[113]:


x=os.listdir(day_dir)
print(x)
os.path.isdir(day_dir+"/"+x[0])


# In[114]:


print(list(recording_sessions))
recording_session_dirs


# In[115]:


len(list(recording_sessions))


# In[ ]:





# In[ ]:





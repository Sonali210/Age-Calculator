#!/usr/bin/env python
# coding: utf-8

# In[159]:


from tkinter import *


# In[160]:


from datetime import date


# In[161]:


root = Tk()


# In[162]:


root.geometry("700x500")


# In[163]:


root.title("Age Calculator")


# In[164]:


def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)


# In[165]:


Label(text="Name").grid(row=1, column=0, padx=90)


# In[166]:


Label(text="Year").grid(row=2, column=0)


# In[167]:


Label(text="Month").grid(row=3, column=0)


# In[168]:


Label(text="Day").grid(row=4, column=0)


# In[169]:


nameValue = StringVar()


# In[170]:


yearValue = StringVar()


# In[171]:


monthValue = StringVar()


# In[172]:


dayValue = StringVar()


# In[173]:


nameEntry = Entry(root, textvariable=nameValue)


# In[174]:


yearEntry = Entry(root, textvariable=yearValue)


# In[175]:


monthEntry = Entry(root, textvariable=monthValue)


# In[176]:


dayEntry = Entry(root, textvariable=dayValue)


# In[177]:


nameEntry.grid(row=1, column=1, pady=10)


# In[178]:


yearEntry.grid(row=2, column=1, pady=10)


# In[179]:


monthEntry.grid(row=3, column=1, pady=10)


# In[180]:


dayEntry.grid(row=4, column=1, pady=10)


# In[181]:


computeButton = Button(text="CalculateAge", command=calculateAge)
computeButton.grid(row=5, column=1, pady=10)


# In[182]:


root.mainloop()


# In[ ]:






# coding: utf-8

# # Tossing a fair coin
# 
# A simple experiment to show that tossing a **fair coin** several times will give a normal distribution.

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# Below a simple function to simulate the tossing of a coin:

# In[29]:


def toss(n):
    r=np.random.rand(1,n)
    #r can be only a number between 0 and 1. If the value is less than 0.5 is 0=head
    # otherwise is 1 =tail (arbitrary, you can change that) 
    return np.round(r) #round to 1 sig.fig


# Image you set up an experiment in which you toss a coin 500 times. The number of tails and heads you will have should be around 50% (due to numerical errors you might not have 50 and 50, but you should expect something close like 49% 51%)

# In[30]:


N=500;
r=toss(N)
n_tails=np.sum(r)
n_head=N-n_tails

print(np.round(n_tails/N*100),np.round(n_head/N*100))


# Now repeat the experiment above 10000 times and store how many tails you have (you can change to head  the same). This is called [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method).

# In[36]:


n_exp=10000

results=[]
for i in range(n_exp):
    r=toss(N)
    results.append(np.sum(r)/N)
    
plt.hist(results)
plt.xlabel('Number of tails')
plt.ylabel('Frequency')


print("median=",np.median(results))    


# Increasing (or decreasing) the number of experiments, it will give you a narrower (or broader) distribution.

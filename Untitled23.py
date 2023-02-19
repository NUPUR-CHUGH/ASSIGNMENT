#!/usr/bin/env python
# coding: utf-8

# In[ ]:



     ASSIGNMENT
    


# In[ ]:


PROBLEM 1


# In[ ]:


#Vwel or consonants
#Write a Python program to check whether an alphabet is vowel or consonant


# In[3]:


letter =input("Enter a Letter: ")
if letter in ['A' ,'E' ,'I' ,'O','U','a','e','i','o','u']:
    print(letter,"is a vowel.")
else:
    print(letter,"is a consonant.")
    


# In[ ]:


PROBLEM 2


# In[4]:


#Write a program to calculatethe sum of n integer number
#Sample Output
#Example:input:2 4 6 8 10
#Output:Sum of the above numbers are : 30


# In[6]:


numbers=input("Enter a list of numbers seperated by spaces: ")
numbers_list=numbers.split()
sum=0
for num in numbers_list:
    sum+=int(num)
print("sum of the numbers are:",sum)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # 1. Write a program (with function) which takes a sequence of numbers and check if all numbers are unique.

# In[1]:


dup_list = [1, 9, 5, 1, 3, 9, 7]
rem_dup = []
for i in dup_list:
    if i not in rem_dup:
        rem_dup.append(i)
print(rem_dup)


# # 2. Python program to find out the average of a set of integers
# a. Note: Don’t use the pre-defined functions like np.mean
# b. For ex: If input is 5, the output should be average of 1+2+3+4+5

# In[6]:


num = [5, 6 , 7, 8 ]
total = int(sum(num))
average = (int(total)/len(num))
print(average)


# # 3. Python program to check whether the given integer is a multiple of both 5 and 7

# In[20]:


for i in range(100):
    if i % 7 == 0 and i % 5 ==0:
        print(i, "is multiple of both 5 and 7 ")

    


# # 4 Python program to display the given integer in reverse manner
# a. Ex: input 852, output should be 258

# In[22]:


input_num = 852
reverse = 0
while(input_num > 0):
    div = input_num % 10
    reverse = reverse*10+div
    input_num = input_num // 10
print(reverse)


# In[24]:


def reverse(num):
   a =str(num)
   revst=a[::-1]
   ans=int(revst)
   return ans
num=852
print(reverse(num))


# # 5. Create an inner function to calculate the addition in the following way
# a. Create an outer function that will accept two parameters, a and b
# b. Create an inner function inside an outer function that will calculate the addition of a 
# and b
# c. At last, an outer function will add 5 into addition and return it

# In[44]:


def outer_fun(a, b):
    square = a ** 2

    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5

result = outer_fun(3, 2)
print(result)


# # 6. Python Program to Check Leap Year
# a. A leap year is exactly divisible by 4 except for century years (years ending with 00). 
# The century year is a leap year only if it is perfectly divisible by 400
# b. For ex: 2017 is not a leap year, 1900 is a not leap year, 2012 is a leap year, 2000 is a 
# leap yea

# In[48]:


def Checkleap(year):
    if((year % 400 ==0) or (year % 100!=0) and (year %4 == 0)):
        print("2022 is a leap year")
    else:
        print("2022 is not a leap year")
result = int(input("enter the year"))
print(Checkleap(result))


# In[ ]:





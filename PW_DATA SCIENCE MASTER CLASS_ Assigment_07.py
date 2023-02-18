#!/usr/bin/env python
# coding: utf-8

# # Assignment_06-02-2023

# ## 1. Creat a function which will take a list as argument and return the product of all the numbers after creating a flat list.
# ## use the below -given list as an argument for your function.
# ### list1=[ 1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,"key2":[55,67,78,89],4:(45,22,61,34)},[56,'data science'],'Mechine Learning']
# 
# ### Note :- you must extract numeric keys and values of the dictionary also.

# In[1]:


def flat_func(list1):
    flat_list=[]
    for i in list1:
        if type(i)== int or type(i)== float:
            flat_list.append(i)
        elif type(i)== list or type(i)==tuple or type(i)==set:
            flat_list.extend(flat_func(i))  ## Extend list by appending elements from the iterable.
        elif type(i)== dict:
            for x in i.keys():
                if type(x)==int or type(x)== float:
                    flat_list.append(x)
            for x in i.values():
                if type(x)== int or type(x)== float:
                    flat_list.append(x)
                elif type(x)== int or type(x)==tuple or type(x)==set:
                    flat_list.extend(flat_func(x))    ## Extend list by appending elements from the iterable.
                    
    return flat_list
list1 = [1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,'key2':[55,67,78,89],4:(45,22,61,34)},[56,'data science'],'Machine Learning']

flat_list=flat_func(list1)
print("flat_list :",flat_list)

result=1
for  i in flat_list:
    result=result*i
print('product of all the number:  ',result)


# ## 2. Write a python Program for encrypting a message sent to you by your friend.The logic of encryption should be such that, for a,the output should be z. for b, the output should be y. for c,the output should be x respectively.Also the whitespace should be repalce with dollar sign. Keep the panchuation mark unchange.
# ## Input sentence : I want to become a Data Scientist.
# ### Encrypt the above input sentence using the program you just created.
# 
# ### Note:- Convert the given input sentence in to lowercase before encripting.The final output should be lower.

# In[2]:


def encrypt_sentence(sentence):
    sentence = sentence.lower() # convert to lowercase
    encrypted_sentence = ""
    for char in sentence:
        if char == " ": # replace whitespace with dollar sign
            encrypted_sentence += "$"
        elif char.isalpha(): # replace letters with corresponding letters from end of alphabet
            encrypted_sentence += chr(122 - ord(char) + 97)
        else: # keep punctuation marks unchanged
            encrypted_sentence += char
    return encrypted_sentence

sentence = input ("Enter teh sentence:   ")
print("Encryption sentance:  ",encrypt_sentence(sentence))


# In[3]:


def flat_func(given_collection):
    flat_list=[]
    for each_element in given_collection:
        if type(each_element)==int or type(each_element)==float:
            flat_list.append(each_element)
        #elif type(each_element)==bool:
         #   flat_list.append(int(each_element))
        elif type(each_element)==list or type(each_element)==set or type(each_element)==tuple:
            flat_list.extend(flat_func(each_element))
        elif type(each_element)==dict:
            for each_nested_element in each_element.keys():
                if type(each_nested_element)==int or type(each_nested_element)==float:
                    flat_list.append(each_nested_element)
            for each_nested_element in each_element.values():
                if type(each_nested_element)==int or type(each_nested_element)==float:
                    flat_list.append(each_nested_element)
                elif type(each_nested_element)==list or type(each_nested_element)==tuple or type(each_nested_element)==set:
                    flat_list.extend(flat_func(each_nested_element))
            
    return flat_list

given_list = [1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,'key2':[55,67,78,89],4:(45,22,61,34)},[56,'data science'],'Machine Learning']

flat_list=flat_func(given_list)

result = 1
for each_element in flat_list:
    result = result*each_element

print('Flat List: ', flat_list)
print('Product of all the numbers: ',result)


# In[4]:


units = int(input("Enter the units of electricity consumed: "))

if units <= 100:
    bill = units * 4.5
elif units <= 200:
    bill = 100 * 4.5 + (units - 100) * 6
elif units <= 300:
    bill = 100 * 4.5 + 100 * 6 + (units - 200) * 10
else:
    bill = 100 * 4.5 + 100 * 6 + 100 * 10 + (units - 300) * 20

print("The total electricity bill is: Rs.", bill)


# In[5]:


total_bill=0;
units=int(input("Enter the um of units comsumed:  "));
i=1;
while i<=units:
    if i<=100:
        total_bill+=4.5;
    elif i>100 and i<=200:
        total_bill+=6;
    elif i>200 and i<=300:
        total_bill+=10;
    else:
        total_bill+=20;
    i+=1;


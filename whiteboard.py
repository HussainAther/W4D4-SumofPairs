#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Your friend has been feeling restless lately and wants to do something, but they have a limited budget and no idea what to do. 
# To help them figure out an activity, you need to create a function. Your friend has given you a list of activities they are interested in(see below)

# Write a function that takes two inputs:

# The type of activity (choose from the activity types listed below)
# The maximum amount of funds available.
# The function should make a request to the Bored API (https://www.boredapi.com/) and retrieve an activity suggestion based on the provided parameters.

# Here are the details:

# Activity Types:

# Recreational
# DIY
# Social
# Cooking
# Music
# Relaxation
# The function should construct the API URL using the provided activity type and maximum price.


# The function should handle the following cases:

# If the provided activity type is valid (one of the activity types listed above) and there is an available activity within the specified price range, the function should return the suggestion in the following format:


# "You should: (activity suggestion)"
# If there is no available activity within the specified parameters, 
# the function should return:

# "Nothing to do!"

# EXAMPLE
# soluion("diy", 20) --> "You should : Make tie dye shirts" 
# "diy" is a valid activity type, and the function returned the activty suggestion of: Make tie dye shirts
# solution("movie",200) --> "Nothing to do!"
# movie is not a valid actvity type and the function returned "Nothing to do!"

# HINT:
# Please ensure that you have the requests library installed before running the code. 
# You can install it by running 'pip install requests' in your terminal or command prompt.
# Retrieve the response as JSON using the response.json() method.


# In[2]:


import requests

def solution(activity_type, max_price):
    activity_url = f"https://www.boredapi.com/api/activity?type={activity_type}&maxprice={max_price}"
    response = requests.get(activity_url)
    data = response.json()

    if response.status_code == 200 and 'activity' in data:
        suggestion = data['activity']
        return f"You should: {suggestion}"
    else:
        return "Nothing to do!"

# In[2]:





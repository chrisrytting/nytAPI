#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests


# In[7]:


# API_KEY = 'v2wsp3yB5OWqhGf99uzEpFaGwddFnyCh'
API_SIGNUP_URL = 'https://developer.nytimes.com/get-started'

class ArchiveAPI():
    def __init__(self, key):
        if key is None:
            raise Exception('Must provide an API key.             If you don\'t have one, go to {} to sign up for one'                            .format(API_SIGNUP_URL))
        else:
            self.key = key
            
    def fetch_articles(self, month, year):
        """
        month: integer 1-12
        year : integer 1851-2019
        
        returns a request object
        """
        
        resp = requests.get('https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}'.format(self.key,year,month))
        if resp.status_code != 200:
            print("Error:")
            if resp.status_code == 401:
                raise Exception('Unauthorized request, check                api-key is set.')
            if resp.status_code == 429:
                raise Exception('Too many requests. You reached                 your per minute or per day rate limit.')
        
                            
        
        


# In[27]:


if __name__ == '__main__':
    for key, value in resp.headers.items():
        print ('Key: {} \t Value: {}'.format(key, value))


    # In[32]:


    type(resp.json())


    # In[40]:


    resp.json()['response'].keys()


    # In[45]:


    len(resp.json()['response']['docs'])


    # In[49]:


    resp.json()['response']['docs'][0]['web_url']


    # In[ ]:





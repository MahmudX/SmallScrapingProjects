#!/usr/bin/env python
# coding: utf-8

# In[60]:


from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from tqdm import tqdm
import pandas as pd
driver = Firefox()
drivertwo = Firefox()


# In[61]:


def get_stat(classItem):
    try:
        return str(company_soup.find('span',{'class':classItem}).text).strip()
    except:
        return None


# In[62]:


df = pd.read_excel('data.xlsx')
counter = 0
for index, row in tqdm(df.iterrows()):
    if counter == 20:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "IP blocked", "Error", 1)
        driver.close()
        drivertwo.close()
        break
    #print(index, row['Company Name'])
    url = "https://www.dnb.com/business-directory/company-search.html?term="+row['Company Name']+"&page=1"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    try:
        counter = 0
        url = "https://www.dnb.com"+str(soup.find('div',{'class':'primary_name'}).find('a')['href']).strip()
        drivertwo.get(url)
        company_soup = BeautifulSoup(drivertwo.page_source,'html.parser')

        dff = pd.DataFrame({'Company Name': row['Company Name'],'Website': row['Website'],'Street Address': str(company_soup.find('div',{'class':'company_street_address'}).text).strip(),"City":get_stat('company_city'),'Zip Code':get_stat('company_postal'),"State":get_stat('company_region'),"Country":get_stat('company_country'),"Tel":print_stat('phone')},index=[0])
        dff.to_csv('res.csv', mode='a', header=False)
    except Exception as e:
        counter+=1
        #print(str(e))
        dff = pd.DataFrame({'Company Name': row['Company Name'],'Website': row['Website'],'Street Address': None, "City":None,'Zip Code':None,"State":None, "Country":None,"Tel":None},index=[0])
        dff.to_csv('res.csv', mode='a', header=False)
    


# In[ ]:





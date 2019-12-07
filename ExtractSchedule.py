from selenium import webdriver
import pandas as pd 
import os


# Configure to use Chrome browser
path = '/Users/teomoney1999/Documents/WebScraping/chromedriver'


driver = webdriver.Chrome(executable_path='/Users/teomoney1999/Documents/WebScraping/chromedriver')
# event_driver = EventFiringWebDriver(driver, MyListener())


# Open the URL 
products = []       # list to store name of the product
prices = []         # list to store price of the product
ratings = []         # list to store rating of the product
driver.get("http://qldt.actvn.edu.vn/CMCSoft.IU.Web.info/Login.aspx")
driver.find_element_by_id('txtUserName').send_keys('CT020201')
driver.find_element_by_id('txtPassword').send_keys('25/02/1999') 
driver.find_element_by_id('btnSubmit').click()

content_path = 'http://qldt.actvn.edu.vn/CMCSoft.IU.Web.Info/Reports/Form/StudentTimeTable.aspx'
driver.get(content_path)

# Get table from web 
table = driver.find_element_by_xpath('//*[@id="gridRegistered"]')


# Return a list of <tr> element
table_data = table.find_elements_by_xpath('.//tr')

# Take the first <tr> element as metadata
list_metadata = table_data[0]

# Set every <td> element from table_data[0] as a list
metadata = list_metadata.find_elements_by_xpath('.//td')

table_format = {}

row_list = [] 
print('=========START==========')
# Get a list of <td> element from each row of table_data[1: len(table_data)] list
for td_data in table_data[1:len(table_data)]: 
    lst = td_data.find_elements_by_xpath('.//td')
    row_list.append(lst)

# Create dict
for i in range(0, len(metadata)): 
    # print('i = ' + str(i))
    # print('metadata length = ' + str(len(metadata)))
    # print('table_data length = ' + str(len(table_data)))
    for j in range(1, len(table_data)-1):
        table_format[metadata[i].text] = row_list[j].text

print(type(table_format))

# Formating data 
df = pd.DataFrame(data = table_format)
df.to_csv("schedule.csv", index=False, encoding='utf-8')

    

    




driver.close()
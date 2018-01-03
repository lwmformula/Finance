
# coding: utf-8

# In[ ]:


from selenium import webdriver
import time
import os.path
import pickle

with open('/Users/Lwmformula/Downloads/intraday_trade/sources/intraday_datalist_yahoo.pkl.txt','r') as f:
    datalist = pickle.load(f)
    
print datalist

for main in datalist:
    test = os.path.isfile('/Users/Lwmformula/Downloads/{}.csv'.format(main)) 
    if test == True: 
        print (main,': No need to update!')
        continue
    driver = webdriver.Chrome()
    driver.set_window_position(0,0)
    driver.set_window_size(1080,900)
    url = "https://finance.yahoo.com/quote/{}/history?period1=0&period2=1502640000&interval=1d&filter=history&frequency=1d"

    driver.get(url.format(main))

    while True:
        try:
            DLink = driver.find_element_by_link_text("Download Data").click()
            time.sleep(2)
        except:
            print ('failed!')
            time.sleep(2)
        test = os.path.isfile('/Users/Lwmformula/Downloads/{}.csv'.format(main)) 
        if test == True: break
    print (main,': Done!')

    driver.quit() 



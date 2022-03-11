from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options

#----------------------------------------

# funcao - test automatico em site via navegador

chrome_options = Options()
chrome_options.add_argument('log-level=0')

#INFO = 0, 
#WARNING = 1, 
#LOG_ERROR = 2, 
#LOG_FATAL = 3.

#----------------------------------------

browser = webdriver.Chrome('./drives/chromedriver')
    # Optional argument, if not specified will search path.
browser.get('https://www.speedtest.net/')
    #navegador.maximize_window() #maximizar a página

avancar = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
avancar.click()
    #clica no GO para executar a busca

site_download = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').get_attribute('result-data-large number result-data-value download-speed')
print(site_download)

#----------------------------------------


#----------------------------------------
#browser.quit()

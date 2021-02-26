from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os


#----------------------------------------
# funcao - test automatico em site via navegador

chrome_options = Options()
chrome_options.add_argument('log-level=3')

#INFO = 0, 
#WARNING = 1, 
#LOG_ERROR = 2, 
#LOG_FATAL = 3.

browser = webdriver.Chrome('./drives/chromedriver')  # Optional argument, if not specified will search path.
browser.get('https://www.speedtest.net/')
#browser.maximize_window() #maximizar a página

#time.sleep(3)
browser = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a') # Já vamos dele
browser.click() # iniciando a função de click armazenada no btn
time.sleep(1)

#----------------------------------------
# excluir o arquivo que baixa no processo

#myfile="C:/Users/douglas.alves/Downloads/px" --compasso
myfile="C:/Users/dougl/Downloads/px"

## If file exists, delete it ##
if os.path.isfile(myfile):
    os.remove(myfile)
else:    ## Show an error ##
    print("Error: %s Arquivo nao encontrado" % myfile)

#----------------------------------------
#browser.quit()

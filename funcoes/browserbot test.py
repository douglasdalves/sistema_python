from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.chrome.options import Options

#----------------------------------------


chrome_options = Options()
chrome_options.add_argument('log-level=0')


#----------------------------------------
def consulta_speed():
    navegador = webdriver.Chrome('./drives/chromedriver')

    navegador.get('https://www.speedtest.net/')
    #navegador.maximize_window() #maximizar a página

    avancar = navegador.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
    avancar.click()
    #clica no GO para executar a busca

consulta_speed()
#site_download = navegador.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').get_attribute('result-data-large number result-data-value download-speed')
#print(site_download)

#----------------------------------------


#----------------------------------------
#browser.quit()

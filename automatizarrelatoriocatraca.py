#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pyautogui as py
import pandas as pd
import sys
from tkinter import *
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver
import time
from datetime import date
from datetime import timedelta

login = "digite aqui"
senha = "digite aqui"

hoje = date.today()
ontem = hoje - timedelta(days = 1)
print(ontem.strftime('%d/%m/%Y'))
######Login#####
driver=webdriver.Edge()
driver.maximize_window()
driver.get('https://192.168.200.2:30443/')
driver.find_element(By.XPATH, '/html/body/div/div[2]/button[3]').click()
driver.find_element(By.XPATH, '/html/body/div/div[3]/p[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/div[1]/input').send_keys(login)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/input').send_keys(senha)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/div[5]/button').click()
time.sleep(3)

####Acessar a guia de relatórios#####
driver.get('https://192.168.200.2:30443/#/view_report/global')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[1]/a[1]').click()

##Trocar para a data desejada##
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[1]/div[1]/div/input').click()
ActionChains(driver)    .key_down(Keys.SHIFT)    .key_down(Keys.HOME)    .key_up(Keys.SHIFT)    .key_up(Keys.HOME)    .perform()
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[1]/div[1]/div/input').send_keys(ontem.strftime('%d/%m/%Y'))
time.sleep(1)
ActionChains(driver)    .key_down(Keys.TAB)    .key_up(Keys.TAB)    .key_down(Keys.TAB)    .key_up(Keys.TAB)    .key_down(Keys.SHIFT)    .key_down(Keys.HOME)    .key_up(Keys.SHIFT)    .key_up(Keys.HOME)    .perform()

##Trocar os para os horários desejados##
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[1]/div/input').send_keys('13:01')
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/input').click()
ActionChains(driver)    .key_down(Keys.SHIFT)    .key_down(Keys.HOME)    .key_up(Keys.SHIFT)    .key_up(Keys.HOME)    .perform()
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[2]/div[2]/div/input').send_keys('13:00')
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[4]/div[2]/div[4]/div/button').click()
time.sleep(3)

####Baixar o relatório####
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/table/thead/tr/th[2]').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[3]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[3]/ul/li[1]/a').click()
time.sleep(2)

####Transformar CSV em TXT####



driver.quit()


# In[25]:





# In[44]:





# In[ ]:





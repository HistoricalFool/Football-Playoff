#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:31:49 2023

@author: alexanderfrei
"""

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

smaller = []
Country = ["aut-bundesliga"]
Year = np.arange(1985, 1993)


for C in Country:
    for y in Year:
        driver.get("https://www.worldfootball.net/all_matches/"+str(C)+"-"+str(y)+"-"+str(y+1)+"-oberes-play-off/")
        driver.implicitly_wait(5)
        
        Time = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(2)")
        Home_team = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(3)")
        Away_team = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(5)")
        Score = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(6)")

        
        for i in range(len(Home_team)):
            

            temporary_data={'Home_team': Home_team[i].text,
                            'Away_team': Away_team[i].text,
                            'Score': Score[i].text,
                            'Time': Time[i].text,
                            'League': C,
                            'Year': y}
            smaller.append(temporary_data)

            
        df_data=pd.DataFrame(smaller)
        df_data.to_excel("~/Football-Playoff/Data/Austria_playoff.xlsx", index=False)

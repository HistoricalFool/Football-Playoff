#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


smaller = []
Country = ["bel-eerste-klasse-a"]
Year = np.arange(2017, 2023)


for C in Country:
    for y in Year:
        driver.get("https://www.worldfootball.net/attendance/bel-eerste-klasse-a-"+str(y)+"-"+str(y+1)+"/1/")
        
        Rank = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(1)")
        Club = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(3)")
        Total = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(4)")
        Matches = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(5)")
        Average = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(6)")
        Year = driver.find_elements(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[3]/h1")
        for i in range(len(Rank)):
            
            print(Total[i].text)
            temporary_data={'Rank': Rank[i].text,
                            'Club': Club[i].text,
                            'Total': Total[i].text,
                            'Matches': Matches[i].text,
                            'Average': Average[i].text,
                            'Year': y}
            smaller.append(temporary_data)
        
        
        
    

        df_data=pd.DataFrame(smaller)
    
        
        df_data.to_csv('~/Football-Playoff/Data/bel-att-rs.csv', index=False)

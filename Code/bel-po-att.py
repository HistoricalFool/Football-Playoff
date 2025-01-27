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
        if y < 2019:
            website = "https://www.worldfootball.net/attendance/bel-eerste-klasse-a-"+str(y)+"-"+str(y+1)+"-playoff-i/1/"
        else:
            website = "https://www.worldfootball.net/attendance/bel-eerste-klasse-a-"+str(y)+"-"+str(y+1)+"-championship/1/"

        driver.get(website)
        
        Rank = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(1)")
        Club = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(3)")
        Total = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(4)")
        Matches = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(5)")
        Average = driver.find_elements(By.CSS_SELECTOR,"#site > div.white > div.content > div.portfolio > div.box > div > table > tbody > tr > td:nth-child(6)")
        for i in range(len(Rank)):
            temporary_data = {
            'Rank': Rank[i].text,
            'Club': Club[i].text,
            'Total': Total[i].text,
            'Matches': Matches[i].text,
            'Average': Average[i].text,
            'Year': y
            }
            smaller.append(temporary_data)
        
    

        df_data=pd.DataFrame(smaller)
    
        
        df_data.to_csv('~/Football-Playoff/Data/bel-po-att.csv', index=False)



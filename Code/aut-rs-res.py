from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Start a Chrome WebDriver session
driver = webdriver.Firefox()

# Open the Bundesliga matchday table URL
url = "https://www.worldfootball.net/schedule/aut-bundesliga-2023-2024-spieltag/22/"
driver.get(url)

# Allow some time for the page to load
time.sleep(3)

# Locate the standings table
table = driver.find_element(By.XPATH, '//div[@class="box"]/table[@class="standard_tabelle"]')

# Get all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skipping the header row

# Prepare data storage
data = []

# Extract data from each row
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    
    if len(cols) < 9:
        continue  # Skip invalid rows
    
    # Extract required information
    position = cols[0].text.strip()
    team = cols[2].text.strip()
    matches = cols[3].text.strip()
    wins = cols[4].text.strip()
    draws = cols[5].text.strip()
    losses = cols[6].text.strip()
    goal_diff = cols[8].text.strip()

    # Append to the list
    data.append([position, team, matches, wins, draws, losses, goal_diff])

# Close the browser
driver.quit()

# Convert to a Pandas DataFrame
df = pd.DataFrame(data, columns=["Position", "Team", "Matches", "Wins", "Draws", "Losses", "Goal Difference"])

# Save to CSV file
csv_filename = "bundesliga_standings.csv"
df.to_csv(csv_filename, index=False)

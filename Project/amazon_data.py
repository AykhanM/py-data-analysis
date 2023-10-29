import pandas as pd
import requests as requests
from bs4 import BeautifulSoup


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")
amazon_data = pd.DataFrame(
    columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text


amazon_data = pd.concat([amazon_data, pd.DataFrame(
    {"Date": date, "Open": Open, "High": high, "Low": low, "Close": close, "Adj Close": adj_close, "Volume": volume}, index=[0])])
print(amazon_data.head())

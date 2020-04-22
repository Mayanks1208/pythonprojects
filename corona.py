import requests
from bs4 import Beatifulsoup
url="https://www.who.int/india/"
r=requests.get(url)
s=Beatifulsoup(r.text,"html.parser")
data=s,find_all("div",class_ = "maincounter-number")

print("Total Cases : " ,data[0].text.strip())
print("Total Deaths : " ,data[1].text.strip())
print("Total Recovered : " ,data[2].text.strip())

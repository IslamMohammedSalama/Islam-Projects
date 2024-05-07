import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

company_names = []
jobs =[]
location_names = []
job_skils = []

# get the link
resalt = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# save the connect 
src = resalt.content

# create the soup object 

soup = BeautifulSoup(src,"lxml")

# find all job postings

jobs = soup.find_all("h2",{"class": "css-noreferrer"})
print(jobs)

# find all com

company_names = soup.find_all("a",{"class": "css-d7j1kk"})
print(company_names)

# find all location names

location_names = soup.find_all("span", {"class": "css-5wys0k"})
# print(location_names)
# find all job skils
job_skils = soup.find_all("div", {"class": "css-1lh32fc"})
# print(job_skils)
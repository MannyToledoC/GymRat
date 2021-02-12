import requests
import os
import time
from bs4 import BeautifulSoup

URL = 'https://wrc.fiu.edu/Program/GetProgramDetails?courseId=3b990f59-63a0-480a-83ab-56f1b0b8e1a5&semesterId=72dc3729-af15-4d58-86ee-7e1aa73e2b50'

title = "GymRat"
message = "Spot Available"
command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
'''


def crawl():
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  result = soup.find(lambda tag:tag.name=="small" and "4:00" in tag.text)
  result = result.find("small")
  return result



def cheese():
  while(True):
    if crawl().text != 'No Spots Available':
      print('Spots Available')
      print (crawl().text)
      os.system(command)
      time.sleep(3600)
    else:
      print('No Spots Available')
      time.sleep(2)

cheese()
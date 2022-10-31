"""
# Save Single Web Page

from pywebcopy import save_webpage

save_webpage(
      url="https://www.australianplantsonline.com.au/tubestockplants.html",
      project_folder="D:/PlantHub/",
      project_name="australianplantsonline",
      bypass_robots=True,
      debug=False,
      open_in_browser=False,
      delay=None,
      threaded=False,
)
"""

import requests
from bs4 import BeautifulSoup

'''
# Scrap from Website

# Configure user agent
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

# Configure URL
url = "https://www.australianplantsonline.com.au/tubestockplants.html"

# Create initial request and save response object
request = requests.get(url, headers=header)

# Parse
parse = BeautifulSoup(markup=request.text, features='html.parser')

# Print
# print(parse.prettify())
'''

# Scrap from Local Copy of Web Page

# Open local copy of web page and parse it
read = open(file='Web Pages/australianplantsonline.html', mode='r')
parse = BeautifulSoup(markup=read, features='html.parser')

# Get the data on basis of attributes 
name = parse.findAll(name='a', attrs={'class' : 'product-item-link'})
price = parse.findAll(name='span', attrs={'class' : 'price'})
description = parse.find_all(name='div', attrs={'class' : 'short'})
image = parse.find_all(name='img', attrs={'class' : 'product-image-photo'})

'''
# Print
for nameitem, priceitem, descriptionitem, imageitem in zip(name, price, description, image):
    print(nameitem.string.strip() + " => " + priceitem.string.strip() + " => " + descriptionitem.string.strip() + " => " + imageitem['src'])
'''

# Write to CSV file
file = open('Data/australianplantsonline.csv', 'a')
for nameitem, priceitem, descriptionitem, imageitem in zip(name, price, description, image):
    file.write('"{}","{}","{}","{}",\n'.format(nameitem.string.strip(), priceitem.string.strip(), descriptionitem.string.strip(), imageitem['src']))
file.close()
"""
# File:             L00162290_Q2_File_2.py
# Created:          08/11/2021, 21:03
# Author:           Gonzalo Roo Ponce
# Student Number:   L00162290
# Version:          1.0.0
# Licensing:        GNU
# Support Contact:  l00162290@student.lyit.ie
# Comments:         
"""

# Calling API #
from bs4 import BeautifulSoup
import requests

# Parsing the VM server website #
apache2 = 'http://192.168.1.169/'
index_doc = requests.get(apache2)
soup = BeautifulSoup(index_doc.text, 'html.parser')

# 2.1 - What are the headings? #
print("Q2.1> All headings in the Apache server webpage are:" )
for divs in soup.findAll(attrs={"class":"section_header"}):
    divs2 = divs.text
    print(divs2.strip())

# 2.2 - Counting how many times Apache2 is present #
# After multiple tries on how to parse the content, the two best headers to search were pre and html #
html = soup.html
html_text = html.text.count('Apache2') + html.text.count('apache2')

pre = soup.pre
pre_text = pre.text.count('Apache2') + pre.text.count('apache2')

apache2total = int(pre_text) + int(html_text)
apache2total = str(apache2total)

print("Q2.2> The total occurrences of the string 'Apache2' (case insensitive) is: " + apache2total)

# 2.3 - Printing all the links for a header #
print("Q2.3> All links in the HTML of the Apache server webpage:")
for a_links in soup.find_all('a'):
    print(a_links.get('href'))







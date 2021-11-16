"""
# File:             l00162290_q2_beautifulsoup4.py
# Created:          08/11/2021, 21:03
# Author:           Gonzalo Roo Ponce
# Student Number:   L00162290
# Version:          1.0.0
# Licensing:        GNU
# Support Contact:  l00162290@student.lyit.ie
# Comments:         
"""

from bs4 import BeautifulSoup
import requests

apache2 = 'http://192.168.1.169/'
index_doc = requests.get(apache2)

soup = BeautifulSoup(index_doc.text, 'html.parser')

#print(soup.prettify())

#!This code scrapes qajarwomen.com

# *Importing required libraries
import urllib.request
import requests
from bs4 import BeautifulSoup
import json

# make a dictionary to fill it later
data = {}
# create a json file
with open('data.json', 'w', encoding='utf-8') as f:
    data['data'] = []
    # main web page for sraping
    main_source = requests.get(
        'http://www.qajarwomen.org/en/people/manifest.html').text
    soup1 = BeautifulSoup(main_source, 'lxml')
    for people in soup1. find_all('li', class_='person_item clearfix'):
        person = people.find('a', class_='person-link')
        personlink = person['href'].split('href=')[-1]
        # a link to each person's web page
        person_link = 'http://www.qajarwomen.org'+personlink
        nameimage = people.find('img', class_='person-image', src=True)
        nameimagelink = nameimage['src'].split('src=')[-1]
        # scrape the image of each person
        if nameimagelink == "/images/noimage.jpg":
            name_image_link = 'http://www.qajarwomen.org'+nameimagelink
        else:
            name_image_link = nameimagelink
        # each person web page for scraping
        person_source = requests.get(
            person_link).text
        soup2 = BeautifulSoup(person_source, 'lxml')
        for page in soup2. find_all('div', class_='twelve columns'):
            # name of each person
            name = page.h2.text
            # print the names just for knowing that the code is running
            print(name)
            # create empty list of relatives for each person to fill it later
            appendedlist = []
            for item in soup2. find_all('div', class_='related-person clearfix'):
                relative = item.find('a', class_='related-person-name').text
                span = item.span.text
                relationship = item.find(
                    'div', class_='related-person-relationship').text
                # updating list of relatives
                relative_name = (relative.replace(
                    relationship, '')).replace(span, '')
                appendedlist.append(relative_name.strip())
            # combine all the scraped data in json format
            data['data'].append({
                'name': name,
                'image': name_image_link,
                'link': person_link,
                'relatives': appendedlist
            })
    # write all the scraped data in json file
    json.dump(data, f, ensure_ascii=False, indent=4)

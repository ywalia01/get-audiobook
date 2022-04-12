from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import os

taskFile = open('tasks.txt', "r")
for line in taskFile:
    
    linksList = []
    file = open('tempFile.txt', "w")
    parentDir = "/Users/yashwalia/Desktop/Audiobooks"
    dirName = ""

    source = requests.get(line).text

    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())

    for x in soup.find_all('title'):
        dirName = x.text

    path = os.path.join(parentDir, dirName)

    try: 
        os.mkdir(path) 
        print("Directory '% s' created" % dirName)
    except OSError as error: 
        print(error)  

    for x in soup.find_all('audio'):
        linksList.append(x.text)

    for x in range(len(linksList)):
        file.write(linksList[x] + "\n")

    file.flush()
    file.close()


    # Opening the text file in read mode to download the links
    sourceFile = open('tempFile.txt', "r")

    for li in sourceFile:
        # print(line)
        ref = li.rfind("/")+1
        filename = li[ref:ref+2]
        print(filename)
        doc = requests.get(li)
        # with open(filename + ".mp3", 'wb') as f:
        #     f.write(doc.content)
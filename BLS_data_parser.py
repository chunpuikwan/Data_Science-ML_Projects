import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
import glob

data_label = ['ln', 'la']                                                           #data_label shows the data we are parsing from BLS website, each shortcut stands for one row in the website. See content.txt
#print(len(data_label))

for f in glob.glob('*.txt'):                                                    #remove all existing files in the directory
    os.remove(f)
'''
#Set the URL you want to webscrape from
url = 'https://download.bls.gov/pub/time.series/ln/'

#Connect to the URL
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')
#print(soup.findAll('a'))

# To download the whole data set, let's do a for loop through all a tags
for i in range(1, len(soup.findAll('a'))):                                      #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    print(link)
    download_url = 'https://download.bls.gov' + link
    urllib.request.urlretrieve(download_url,link[link.find('/ln.') + 1:])       #download data from download_url and save into a filename
    time.sleep(1)                                                               #pause the code for a sec to prevent the website consider us as a scammer


files = glob.glob('ln*')                                                        #rename all files and put them into .txt files
for file in files:
    #parts = file.split('.')
    #new_name = 'year_{}'.format(parts[1])
    #os.rename(file,new_name)
 
    #Attempted correction for my purpose
    #parts = file.split('.')
    #parts_len = len(parts)
    #new_name = 'year_{}'.format(parts[1])
    #os.rename(file,new_name)
    os.rename(file, file.replace('.','_') +'.txt')

'''
#define parser function
def parser(var):
    url = 'https://download.bls.gov/pub/time.series/' + var + '/'
    #Connect to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.findAll('a')
    #print(soup.findAll('a'))

    # To download the whole data set, let's do a for loop through all a tags
    for i in range(1, len(soup.findAll('a'))):                                                     #'a' tags are for links
        one_a_tag = soup.findAll('a')[i]
        link = one_a_tag['href']
        if link == '/pub/time.series/la/maps/':
            pass
        else:
            download_url = 'https://download.bls.gov' + link
            urllib.request.urlretrieve(download_url,link[link.find('/'+ var +'.') + 1:])       #download data from download_url and save into a filename
            time.sleep(1)                                                                              #pause the code for a sec to prevent the website consider us as a scammer
    return  

#define function to rename each file
def rename(data_label_shortcut):
    files = glob.glob(data_label_shortcut +'*')                                                        #rename all files and put them into .txt files
    for file in files:
        #parts = file.split('.')
        #new_name = 'year_{}'.format(parts[1])
        #os.rename(file,new_name)
        
        #Attempted correction for my purpose
        #parts = file.split('.')
        #parts_len = len(parts)
        #new_name = 'year_{}'.format(parts[1])
        #os.rename(file,new_name)
        os.rename(file, file.replace('.','_') +'.txt')
    return

for p in range(0, len(data_label)):
    data_label_shortcut = data_label[p]
    parser(data_label_shortcut)
    rename(data_label_shortcut)


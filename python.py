
from bs4 import BeautifulSoup
  
HTMLFile = open("name_of_your_file.html", "r", encoding="utf8")

index = HTMLFile.read()

S = BeautifulSoup(index, 'lxml')

list=[]

tag_name = S.find_all('div')

for tag in tag_name:
    if 'tag_name=' in str(tag): # define your custom tag name
        tag=str(tag)
        sencha = tag.partition("tag_name=")[2] # and here
        sencha = sencha.split("\"")[1]
        list.append(sencha)
        
for i in list:
    print(i)

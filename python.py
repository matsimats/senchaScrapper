# Wymaga zainstalaowania bibliotek bs4
# Importujemy BeautifulSoup class z modułu bs4
from bs4 import BeautifulSoup
  
# Otwarcie pliku HTML aplikacja.html
HTMLFile = open("kontakty.html", "r", encoding="utf8")
  
# Odczyt
index = HTMLFile.read()
  
# Tworzymy obiekt BeautifulSoup i definiujemy parser
S = BeautifulSoup(index, 'lxml')

# Lista do trzymania wartości
list=[]

# Szukamy Div'ów
tag_name = S.find_all('div')
for tag in tag_name:
    # Szukamy Senchatestów wewnątrz Divów
    if 'senchatest' in str(tag):
        tag=str(tag)
        # Rozdzielenie Senchatest
        sencha = tag.partition("senchatest=")[2]
        # Wyciągamy wartości przed "senchatest="
        sencha = sencha.split("\"")[1]
        # Dodanie do listy
        list.append(sencha)
'''
Listujemy:
print('senchatest=blaBlaBla')
'''

for i in list:
    print(i)

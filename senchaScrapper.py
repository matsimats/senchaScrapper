
from bs4 import BeautifulSoup
import xlsxwriter

class phraser():
    def go(self):
        self.HTMLFile = open("file.html", "r", encoding="utf8")
        self.index = self.HTMLFile.read()
        self.S = BeautifulSoup(self.index, 'lxml')
        self.list=[]
        self.tag_name = self.S.find_all('div')

        for self.tag in self.tag_name:
            if 'senchatest=' in str(self.tag):
                self.tag=str(self.tag)
                self.sencha = self.tag.partition("senchatest=")[2]
                self.sencha = self.sencha.split("\"")[1]
                self.list.append(self.sencha)

        for i in self.list:
            print(i)

    def excel(self):
        self.outWorkbook = xlsxwriter.Workbook("out2.xlsx")
        self.outSheet = self.outWorkbook.add_worksheet()
        self.value = self.list
        self.outSheet.write("A1", "senchatest")
        self.outSheet.write("B1", "second")
        self.outSheet.write("C1", "third")

        for item in range (len(self.list)):
            self.outSheet.write(item+1, 0, self.list[item])

        self.outWorkbook.close()

phraser = phraser()
phraser.go()
phraser.excel()

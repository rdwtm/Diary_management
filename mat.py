import csv
from os.path import  exists



class cms:
    def __init__(self,file):
        self.filename=file
        self.tab=[]
    def File_exist(self):
        return exists(self.filename)
    def Add_cow(self,id,date):
        self.tab.append([id,date])
    def Save_tab(self,mode):
        with open(mat.filename, mode, encoding='utf-8') as csvfile:
            # inicjujemy *zapisywacz*
            csvwriter = csv.writer(csvfile)
            # wpisujemy pierwsza linie naszego pliku CSV (nazwy kolumn)
            for row in self.tab:
                csvwriter.writerow(row)
    def Read_file(self):
        with open(mat.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            i=1
            tab=[]
            print('---------------------------------------------------')
            for row in csvreader:
                print(i,':  ',*row) # wartość kolumny 1 z tego wiersza
                i+=1
                tab.append(row)
            self.tab=tab
    def Load_file(self):
        with open(mat.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                tab=[]
                tab.append(row.split())
                self.tab=tab
    def Delete_cow(self):
        self.Read_file()
        print('---------------------------------------------------')
        x=(int(input('Ktory wpis usunac?'))-1)
        self.tab.pop(x)
        self.Save_tab('w')





mat=cms('cow.csv')
while True:
    match(input("""
    1. Odczyt pliku:   
    2. Dodaj sztuke:   
    3. Usun sztuke:
    Nascisnij q zeby zamknac     
    """)):
        case ('1'):
            if mat.File_exist():
                mat.Read_file()

        case ('2'):
            print('---------------------------------------------------')
            id, dat = input('wpisz ID oraz date oddzielajac przecinkiem').split()
            mat.Add_cow(id,dat)
            mat.Save_tab('a')
            print('dodano')

        case ('3'):
            mat.Delete_cow()

        case ('q'):
            break




# if mat.File_exist():
#     print('tak')
# else:
#     mat.Add_cow('id','date')
#     mat.Save_tab()
#     print('dodano')



















# if File_exist('plik.csv'):
#     with open('plik.csv', 'r', encoding='utf-8') as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=',')
#         # for row in csvreader:
#         #     print(row[0]) # wartość kolumny 1 z tego wiersza
#         #     print(row[1]) # analogicznie - 2 kolumna
#         #     print(row[2]) # 3cia
# else:
#     with open('plik.csv', 'w', encoding='utf-8') as csvfile:
#         # inicjujemy *zapisywacz*
#         csvwriter = csv.writer(csvfile)
#         # wpisujemy pierwsza linie naszego pliku CSV (nazwy kolumn)
#         csvwriter.writerow(['kolumna 1', 'kolumna 2', 'kolumna 3'])
#         # czas na kolejne linie z wartosciami
#         csvwriter.writerow(['wartosc1_kol1', 'wartosc1_kol2', 'wartosc1_kol3'])
#         csvwriter.writerow(['wartosc2_kol1', 'wartosc2_kol2', 'wartosc2_kol3'])
#         csvwriter.writerow(['wartosc3_kol1', 'wartosc3_kol2', 'wartosc3_kol3'])



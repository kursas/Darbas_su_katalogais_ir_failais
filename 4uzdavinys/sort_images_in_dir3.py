#sort images in dirs
import os,time
import datetime
import shutil

#p='E:/1'
p=input('Nukopink kelia iki nuotraukų. Pavyzdžiui: pvz:(D:/DUMENYS/DARIUS/Desktop/otsl2):')
os.chdir(p)

#создаем папки месяцев от 01 до 12
def d():
    for x in range (1,13):
        if x>9:
            if not os.path.exists(str(x)):
                os.makedirs(str(x))
        else:
            if not os.path.exists('0'+str(x)):
                os.makedirs('0'+str(x))

def mod_date(file):
    t = os.path.getmtime(file)
    return datetime.datetime.fromtimestamp(t)

#sukurem folderius su metais ir juose įdetų menesių folderiais
# perskaitem metus folderyje su foto
#sužinojom pletinius visų folderyje esančių failų
#images=['JPG','jpg']
a=[] #['AAE', 'MOV', 'JPG', 'PNG']
for root, dirs, files in os.walk(p):    
    for file in files:
        if file[-3:] not in a:
            a.append(file[-3:])
        if file[-3:] in a:
            year=str(mod_date(file))[:10][:4]            
            if not os.path.exists(year):
                os.makedirs(year)
            os.chdir(p+'/'+year)            
            d()
            os.chdir(p)


#perkelem failus iš esamo folderio į sukurtus menesių ir metų folderius
try:
    for root, dirs, files in os.walk(p):    
        for file in files:
                if file[-3:] in a:
                    year=str(mod_date(file))[:10][:4]                    
                    month=str(mod_date(file))[:10][5:7] #menuo nuotraukų sudaryti
                    shutil.move(file, year+'/'+month+'/'+file) #perkele failą į folderį
except EnvironmentError:
    print('Atrodo,susitvarkem!!')
#output
#Nukopink kelia iki nuotraukų. Pavyzdžiui: pvz:(D:/DUMENYS/DARIUS/Desktop/otsl2):D:/DUMENYS/DARIUS/Desktop/otsl2
#Atrodo,susitvarkem!!
#Process finished with exit code 0


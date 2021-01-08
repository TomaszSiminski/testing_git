import cgi
import sys
import os
import subprocess
import re
import cgitb #for addirional infoin case of errors
cgitb.enable()


# 1. Otworzyc plik opcji
f = open("MLM.opt","r",encoding="utf-8")
file_content = f.readlines()
f.close()

# 2. Wyszukac linie poczatek od GROUP

line_start_GROUP = []
list_of_user = []


for line in  file_content:
    if line.startswith('GROUP'):
        #print(line)
        line_start_GROUP = line.split() 
        if len(line_start_GROUP)>2:  #protect for line without users
            licznik = 0
            for user in line_start_GROUP:
                if licznik>1:               #read from third element of list in line
                    #print(line_start_GROUP[licznik])
                    list_of_user.append(line_start_GROUP[licznik])  # create list of users - not unique yet
                licznik += 1
            # print(len(line_start_GROUP))
            # print(line_start_GROUP[len(line_start_GROUP)-1])
            # print(line)
                
                
                
# 3. Zbudowac listę uzytkowników - unikalne nazwy - przegląd po liniach z pkt 3
                
unique_list_of_user = list(set(list_of_user))   #remove duplicate from list_of_user
#print(unique_list_of_user)


# 4. Majac liste unikalnych userów - przeszukac linie i zbudować słownik  user: [lista opcji]
result = {}
#print(file_content)


# for user in unique_list_of_user:
    # result[user] = ''
    # print(result)
    # print(type(result))




for user in unique_list_of_user:
    #print(user)
    list_for_one_user = []  #create temporary list for one user
    for line in  file_content:
        #print(line)
        if user in line:
            line_start_GROUP = line.split()
            list_for_one_user.append(line_start_GROUP[1])  # creating list of features
    #print(list_for_one_user)
    result[user] = list_for_one_user

# for user in unique_list_of_user:
    # print(user+': ',end='')
    # for l in result[user]:
        # print(l,end=';')
    # print('')
            
            

# print(result)

    
print("Content-Type: text/html\r\n\r\n")
print("<html><body>")
print('<p>')

for user in unique_list_of_user:
    #print(user+': ',end='')
    print("{}: ".format(user))
    for l in result[user]:
        print(l,end=';')
    print('<br>')

print('<p>')
print("</body></html>")








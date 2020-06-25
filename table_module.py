import requests
import lxml.html as lh
import pandas as pd
import json
import numpy as np
from bs4 import BeautifulSoup

#Scrapping tabele from website

url='http://lotobayisi.com/Sayisal-Butun-Veriler.aspx'
#url='http://lotobayisi.com/Super-Butun-Veriler.aspx'
#url='http://lotobayisi.com/Sans-Topu-Butun-Veriler.aspx'
#url='http://lotobayisi.com/On-Numara-Butun-Veriler.aspx'
                
# Create a page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')


#Check first 12 rows for Sayısal Loto
print("Sayısal Loto satır kontrol: ")
[len(T) for T in tr_elements[:12]]


tr_elements = doc.xpath('//tr')

#Create empty list
col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))


#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 8, the //tr data is not from our table 
    if len(T)!=8:
        break
        
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        
        #Check if row is empty
        if i>0:
     
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
            
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1


print("Sayısal Loto data kontrol - 1")
[len(C) for (title,C) in col]


#Create Sayısal Loto dataframe
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)


df.head()


len(df)


#Change column names
df.columns=['Hafta', 'Tarih', 'Sayi1', 'Sayi2', 'Sayi3', 'Sayi4', 'Sayi5', 'Sayi6']

#Remove \r\n from the table
df = df.replace('\r\n','', regex=True)
df = df.replace(' ','', regex=True)

df.head()


#Drop duplicate weeks from the dataframe
df.drop_duplicates(subset='Hafta', inplace=True, keep='first')


print("Sayısal Loto data kontrol")
len(df)


df.head()


#Create an empty list 
row_list =[] 
  
#Iterate over each row 
for index, rows in df.iterrows(): 
    #Create list for the current row 
    list =[rows.Sayi1, rows.Sayi2, rows.Sayi3, rows.Sayi4, rows.Sayi5, rows.Sayi6] 
    #Append the list to the final list 
    row_list.append(list) 
  
#Print the list 
print(row_list) 

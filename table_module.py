import requests
import lxml.html as lh
import pandas as pd
import json
import numpy as np
from bs4 import BeautifulSoup

#Scrapping tabele from website
url='http://lotobayisi.com/Sayisal-Butun-Veriler.aspx'

class tableScrap:
    def __init__(self, url):
        self.url = url
        
    def func(url):
                
        # Create a page, to handle the contents of the website
        page_sayisal = requests.get(url)
        
        #Store the contents of the website under doc
        doc_sayisal = lh.fromstring(page_sayisal.content)
        
        #Parse data that are stored between <tr>..</tr> of HTML
        tr_elements_sayisal = doc_sayisal.xpath('//tr')
        
        
        #Check first 12 rows for Sayısal Loto
        print("Sayısal Loto satır kontrol: ")
        [len(T_sayisal) for T_sayisal in tr_elements_sayisal[:12]]
        
        
        tr_elements_sayisal = doc_sayisal.xpath('//tr')
        
        #Create empty list
        col_sayisal=[]
        i=0
        
        #For each row, store each first element (header) and an empty list
        for t_sayisal in tr_elements_sayisal[0]:
            i+=1
            name_sayisal=t_sayisal.text_content()
            print('%d:"%s"'%(i,name_sayisal))
            col_sayisal.append((name_sayisal,[]))
        
        
        #Since out first row is the header, data is stored on the second row onwards
        for j_sayisal in range(1,len(tr_elements_sayisal)):
            #T is our j'th row
            T_sayisal=tr_elements_sayisal[j_sayisal]
            
            #If row is not of size 8, the //tr data is not from our table 
            if len(T_sayisal)!=8:
                break
                
            #i is the index of our column
            i=0
            
            #Iterate through each element of the row
            for t_sayisal in T_sayisal.iterchildren():
                data_sayisal=t_sayisal.text_content() 
                
                #Check if row is empty
                if i>0:
             
                #Convert any numerical value to integers
                    try:
                        data_sayisal=int(data_sayisal)
                    except:
                        pass
                    
                #Append the data to the empty list of the i'th column
                col_sayisal[i][1].append(data_sayisal)
                #Increment i for the next column
                i+=1
        
        
        print("Sayısal Loto data kontrol - 1")
        [len(C_sayisal) for (title,C_sayisal) in col_sayisal]
        
        
        #Create Sayısal Loto dataframe
        Dict_sayisal={title:column for (title,column) in col_sayisal}
        df_sayisal=pd.DataFrame(Dict_sayisal)
        
        
        df_sayisal.head()
        
        
        len(df_sayisal)
        
        
        #Change column names
        df_sayisal.columns=['Hafta', 'Tarih', 'Sayi1', 'Sayi2', 'Sayi3', 'Sayi4', 'Sayi5', 'Sayi6']
        
        #Remove \r\n from the table
        df_sayisal = df_sayisal.replace('\r\n','', regex=True)
        df_sayisal = df_sayisal.replace(' ','', regex=True)
        
        df_sayisal.head()
        
        
        #Drop duplicate weeks from the dataframe
        df_sayisal.drop_duplicates(subset='Hafta', inplace=True, keep='first')
        
        
        print("Sayısal Loto data kontrol")
        len(df_sayisal)
        
        
        df_sayisal.head()
        
        
        #Create an empty list 
        row_list_sayisal =[] 
          
        #Iterate over each row 
        for index, rows in df_sayisal.iterrows(): 
            #Create list for the current row 
            list_sayisal =[rows.Sayi1, rows.Sayi2, rows.Sayi3, rows.Sayi4, rows.Sayi5, rows.Sayi6] 
            #Append the list to the final list 
            row_list_sayisal.append(list_sayisal) 
          
        #Print the list 
        print(row_list_sayisal) 
        return(row_list_sayisal)
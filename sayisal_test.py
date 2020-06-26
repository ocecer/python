#Required installations
#!conda install -c anaconda lxml --yes
#!conda install -c conda-forge BeautifulSoup4 --yes
#!conda install -c conda-forge html5lib --yes
#!conda install -c conda-forge request --yes
#!conda install -c anaconda lxml --yes

print("Yüklemeler tamamlandı!")

#import requests
#import lxml.html as lh
#import pandas as pd
#import json
#import numpy as np
#from bs4 import BeautifulSoup
import random
import sayisalLotoModule as say

print("Sayisal Loto = 1\nExit = 0\n")

while True:
    
    numbers=[]
    i=1

    gameType = int(input("which game would you like to play: "))

    if gameType == 0:
        print("Bye!")
        break

    if gameType == 1:
        columnNumber = int(input("\nHow many columns would you like to play: "))
        numbers=list(range(1,49))   
        
        url='http://lotobayisi.com/Sayisal-Butun-Veriler.aspx'

            
        while i <= columnNumber:
            chosenNumbers=random.sample(numbers,6)
            chosenNumbers.sort() 
        
            if chosenNumbers in say.row_list:
                print(f"{i}. Kolon: {chosenNumbers} This combination have won before!")
                
            
            else:
                print(f"{i}. Kolon: {chosenNumbers}")
                
            i+=1
        continue
    
    
#    else:
#        print("Lütfen oyun kodunu doğru giriniz.")
#        continue

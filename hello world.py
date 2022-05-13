#Autor:Edelmann Patrick; Simon Angerer
#Datum:13.05.2022
#Simply Python Programm Hi World!

import time
s=time.time()
n=input("Namen eingeben:")
print(n)
e=time.time()
dif=round(e-s,1)
print("Zeit",dif,"sek")
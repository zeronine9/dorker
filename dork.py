from googlesearch import *

mylist = [] 

try :
    a = input("Enter the dork here : ")
    b = int(input("Enter Number of web sites you want : "))

    for url in search(a,stop=b):
        print(url)
        mylist.append(url)
except ValueError:
    print("Pleace Enter a Number ")

zahir = open("results.txt","w")
for item in mylist:
    zahir.write(str(item))
    zahir.write("\n")
    
zahir.close()

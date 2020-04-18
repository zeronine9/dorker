from googlesearch import *

try :
    a = input("Enter the dork here : ")
    b = int(input("Enter Number of web sites you want : "))

    for url in search(a,stop=b):
        print(url)
except ValueError:
    print("Pleace Enter a Number ")

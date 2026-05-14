import os

file = open("example.txt","r")

file.close()

with open("example.txt","x") as file:
    content = file.read()
    print(content)

with open("example.txt","w") as file:
    file.write("hello from main")

lista = ["hello world!\n", "Welcome to python!\n"]

with open("example.txt","w") as file:
    file.writelines(lista)


if os.path.exists("example.txt"):
    print("file ekziston")

if os.path.exists("dfdf.txt"):
    print("file ekziston")
else:
    print("file nuk ekziston")

with open("example.txt","a") as file:
    file.write("hello from main")

name="Donjeta"
age=232323

with open("output.txt","") as file:
    file.write("Name:" + name + "\n")
    file.write("Age:" + str(age) + "\n")

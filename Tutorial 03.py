# for loop 1

names = ["Tim", "Brian", "Mike", "John"]

for name in names:
    print(name)
    


# for loop 2
names = ["Tim", "Brian", "Mike", "John"]
ages = ["15", "20", "30", "56"]

for i in range(len(names)):
    print(names[i] + ages)
    
    
    
# while loop

name = ""
while name != "Tim":
    name = input("what is your name: ")
    
    
    
# try & except

number = input("Type a number: ")

try:
    float(number)
    print("it is a number! ")
except:
    print("please type a number")
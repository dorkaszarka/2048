userinput = input("Enter an operation(add, list, mark, archive): ")

if userinput == "add":
    newitem = input("Add an item: ")
    todolist = open("todolist.txt" , "a+")
    todolist.writelines (" [ ] " + (newitem) + "\n")

if userinput == "list":
    todolist = open("todolist.txt", "r")
    list =  todolist.read()
    print(list)
    
if userinput == "archive":
    item = open("todolist.txt" , "r")
    lines = item.readlines()
    item.close()
    item = open("todolist.txt" , "w")

for line in lines:
    if line!="[x]":
        item.write(line)
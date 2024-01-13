while True :
    name = input("What is your name? ")
    if name == "" :
        print("This field can't be empty")
        continue
    else :
        break

length = len(name)

print("Hello," , name ,", nice to meet you!")
print("Your name has" , length ,"letters!")

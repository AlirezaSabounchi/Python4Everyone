while True :
    amount = input("Enter bill amount :")
    try :
        amount = int(amount)
    except :
        print("Invalid input,Try Again!")
        continue

    rate = input("Enter tip rate :")
    try :
        rate = int(rate)
        break
    except :
        print("Invalid input,Try Again!")
        continue

tip = amount * rate/100

print("You should tip" , tip , "$")

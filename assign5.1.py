number = None
largest = -1
smallest = None
while number!= 'done' :
    number = input ("Enter Number:")
    if number == 'done':
        break
    else:
        try:
            integ = int(number)
        except:
            print("Invalid input")
            continue
        if smallest is None :
            smallest = integ
        if largest < integ :
            largest = integ
        elif smallest > integ:
            smallest = integ
print("Maximum is " , largest)
print("Minimum is " , smallest)

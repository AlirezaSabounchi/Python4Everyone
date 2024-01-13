def computepay(h,r):
    if h <= 40:
        pay = h*r
    else :
        pay = (40 * r) + (h-40)*r*1.5

    return(pay)

hrs = input('Enter Hours :')
try:
    h = float(hrs)
except:
    print('Please Enter a Valid Number')
    quit()

rate = input('Enter rate :')
try:
    r = float(rate)
except:
    print('Please Enter a Valid Number')
    quit()

pay = computepay(h,r)
print("Pay" , pay)

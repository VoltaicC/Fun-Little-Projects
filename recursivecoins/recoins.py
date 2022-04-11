#good luck
def r(m):
    if(int(m/25)>0):
        print(int(m/25), " quarters")
        r(m%25)
    elif(int(m/10)>0):
        print(int(m/10), " dimes")
        r(m%10)
    elif (int(m/5)>0):
        print(int(m/5), " nickels")
        r(m%5)
    else:
        print(m, " pennies")
r(int(100*(float(input()))))

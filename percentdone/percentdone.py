import time

dailyHours = float(input("Enter amount of hours you will work: "))
seconds = float(input("Enter number of minutes already worked today: ")) * 60 


while (seconds < (dailyHours * 3600)):
    #print((seconds / (dailyHours * 3600)))
    print("{:.4f}".format(100 * (seconds / (dailyHours * 3600))) + "%")
    time.sleep(1)
    seconds = seconds + 1
print("100%")
print("Congrats, you are free")
input()

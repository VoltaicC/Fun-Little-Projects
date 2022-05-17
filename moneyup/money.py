import time

money = 0.00
hourlyRate = float(input("Enter your hourly rate: "))
dailyHours = float(input("Enter amount of hours you will work: "))


while (money < (hourlyRate * dailyHours)):
    print("{:.2f}".format(money))
    time.sleep(1)
    money = money + hourlyRate/3600
print("Congrats, you are free")
input()

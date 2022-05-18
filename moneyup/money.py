import time


hourlyRate = float(input("Enter your hourly rate: "))
dailyHours = float(input("Enter amount of hours you will work: "))
money = float(input("Enter number of minutes already worked today: ")) * 60 * (hourlyRate/3600);


while (money < (hourlyRate * dailyHours)):
    print("{:.2f}".format(money))
    time.sleep(1)
    money = money + hourlyRate/3600
print("Congrats, you are free")
input()

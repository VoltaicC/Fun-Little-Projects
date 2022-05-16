import time

money = 0.00
hourlyRate = 17.00
dailyHours = 8

while (money < (hourlyRate * dailyHours)):
    print("{:.2f}".format(money))
    time.sleep(1)
    money = money + hourlyRate/3600

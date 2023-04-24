import time

password = int(input("Enter a number: "))
num = 0
#start timer
start = time.time()
while num != password:
    num += 1
#end timer
print(f'Cracked password is {num}!')
end = time.time()
print("Time elapsed: " + str(end - start))
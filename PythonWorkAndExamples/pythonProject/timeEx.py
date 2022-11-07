import time

initial = time.time()
print("This is a starting time:- ", initial, "\n")

k = 0
while (k < 5):
    print("This is while loop")
    time.sleep(1)
    k += 1
print("This is a initial time of while loop", time.time() - initial, "Seconds\n")

initial2 = time.time()
for i in range(5):
    print("This is a jerry")
print("This is a initial time of for loop", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
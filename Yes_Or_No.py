import time
import math
start = time.time()
period_of_time = 1.33333333333333333333333333333333333333333333333
primes = [2]
x = 3
while True:
    p = 1
    for i in primes:
        if p == len(primes):
            primes.append(x)
            break
        elif x%i != 0:
            p += 1
    x += 1
    if time.time() > start + period_of_time:
        if math.floor(pow(1.001,primes[-1]))%2==0:
            print("Yes")
        else:
            print("No")
        break
input()

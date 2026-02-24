print("Prime Range Analyzer")

start = int(input("Enter start: "))
end = int(input("Enter end: "))

num = start
prime_count = 0

while num <= end:
    if num > 1:
        i = 2
        flag = 0

        while i * i <= num:
            if num % i == 0:
                flag = 1
                break
            i = i + 1

        if flag == 0:
            print("Prime:", num)
            prime_count = prime_count + 1

    num = num + 1

print("Total primes:", prime_count)

if prime_count > 10:
    print("Many primes")
else:
    print("Few primes")
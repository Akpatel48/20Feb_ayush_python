#Write a Python program to returns sum of all divisors of a number

number = int(input("enter a number: "))
divisor_sum = 0
for i in range(1, number+1):
    if number % i == 0:
        divisor_sum += i
    
print(f"sum of divisors:{number}")

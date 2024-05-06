#Write a Python program to returns sum of all divisors of a number

number = int(input("enter a number: "))     #get number
divisor_sum = 0
for i in range(1, number+1):
    if number % i == 0:     #check number is divisors or not
        divisor_sum += i    #sum of divisors number
    
print(f"sum of divisors:{divisor_sum}")  

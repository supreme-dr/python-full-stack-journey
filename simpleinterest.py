def simple_interest(p, r, t):
    return (p * r * t) / 100
# Example usage:
# principal = 1000  
# rate = 5  
# time = 3      
# interest = simple_interest(principal, rate, time)
# print(f"The simple interest is: {interest}")# Variables and printing
name = "Emmanuel"
age = 20    
principal = 1000
rate = 50
time = 12
interest = simple_interest(principal, rate, time)
print (f"My name is {name} and I am {age} years old")
print(f"The simple interest is: {interest}")
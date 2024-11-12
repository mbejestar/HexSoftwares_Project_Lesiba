def fibonacci(n):  
    fib_sequence = []  
    
    a, b = 0, 1  
    for _ in range(n):  
        fib_sequence.append(a)  
        a, b = b, a + b  
        
    return fib_sequence  

# Get user input for the number of Fibonacci numbers to generate  
try:  
    count = int(input("Enter the number of Fibonacci numbers to generate: "))  
    if count < 0:  
        print("Please enter a non-negative integer.")  
    else:  
        print(f"Fibonacci series up to {count} terms:")  
        print(fibonacci(count))  
except ValueError:  
    print("Invalid input! Please enter a positive integer.")
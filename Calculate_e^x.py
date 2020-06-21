def exponential(n, x): 

    sum = 1.0 
    for i in range(n, 0, -1): 
        sum = 1 + x * sum / i 
    print ("e^x =", sum) 

n = 10
x = 1.0
exponential(n, x) 

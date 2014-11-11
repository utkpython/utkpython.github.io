import matplotlib.pyplot as plt

def collatz(x):
    if x%2 == 0:
        x = x/2
    else:
        x = 3*x + 1
    return x

def no_collatz(x):
    index = 0
    while x > 1 :
        x = collatz(x)
        index = index + 1
    return(index)

def no_collatzto(n):
    indicees = []
    for i in range(1,n+1):
        a = no_collatz(i)
        indicees.append(a)
    return indicees

def plot_collatz(n):
    import matplotlib.pyplot as plt
    plt.scatter(range(1,n+1),no_collatzto(n))

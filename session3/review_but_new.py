#################
# functions can
# return multiple
# things. What
# does this do?

def func(x):
    return x**3, "%s" %x, x+1
    
#################
# anonymous
# functions are 
# very handy

anon = lambda x: x**2 + (1.)/x

################
# what does the 
# following do?

my_funky_list = [anon(i) for i in range(1,100)]


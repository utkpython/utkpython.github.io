def is_prime(number):
    '''returns true if an integer is prime
    returns false otherwise'''
    if (type(number) != int) or (number == 1):
        return False
    if number%2==0 and number!=2:
        return False
    for divisor in range(3,int(number**0.5)+1,2):
        if number%divisor==0:
            return False
    return True
    
def gen_prime_list(upper_limit):
    '''Generates a list of prime numbers up 
       upper_limit
       Example:
            gen_prime_list(10) returns
            [2,3,5,7]'''
    prime_list = []
    for i in range(upper_limit + 1):
        if is_prime(i) == True:
            prime_list.append(i)
    return prime_list

def distance_between(prime_list):
    '''gives list of distances between prime_list
       distance_between([2,3,5,7]) will return
       [1,2,2]'''
    dist = []
    for i in range(len(prime_list)-1):
        dist.append(prime_list[i+1] - prime_list[i])
    return dist

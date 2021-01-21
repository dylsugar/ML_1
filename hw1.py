import numpy as np

# Question 1(a)
def prime_nums_reversed(n):
    '''
        Write a function nums_reversed that takes in an integer n and returns a string containing all prime numbers between 1 and n in reverse order, separated by spaces. For example:
            >>> prime_nums_reversed(5)
            '5 3 2 1'
        Note: The ellipsis (...) indicates something you should fill in. It doesn't necessarily imply you should replace it with only one line of code.
    '''

    #primes = []
    #last_prime = [True] * (n + 1)
    #for p in range(2, n + 1):
    #    if (last_prime[p]):
    #        primes.append(p)
    #    for i in range(p ** 2, n + 1, p):
    #       last_prime[i] = False
    
    #primes.reverse()
    #result = " ".join(str(e) for e in primes)
    i = 0
    j = 0
    f = 0
    prime = []
    for i in range(1, n+1, 1):
        if i == 1 or i == 0:
            continue
        f = 1

        for j in range(2, (i // 2 ) + 1, 1):
            if i % j == 0:
                f = 0
                break

        if flag == 1:
            prime.append(i)
    prime.reverse()
    result = " ".join(str(e) for e in prime)
    return result


# Question 1(b)
def string_explosion(string):
    '''
        Write a function string_explosion that takes in a non-empty string like "Code" and returns a long string containing every suffix of the input. For example:
        >>> string_explosion('Code')
        'Codeodedee'
        >>> string_explosion('data!')
        'data!ata!ta!a!!'
        >>> string_explosion('hi')
        'hii'
        Hint: Try to use recursion.
    '''

def string_explosion(string):
    if string == '':
        return ''
    else:
        if string == None:
            return ''
        else:
            return string + string_explosion(string[1:])


# Question 1(c)
def replace(a, b):
    '''
        Write a function `replace` that takes in two lists: `a` and `b`, and returns a list where the last element of `a` is replaced by the list `b`.

        >>> replace([1, 2, 3, 4], [5, 6, 7, 8])
        [1, 2, 3, 5, 6, 7, 8]
        >>> replace([8, 4, 3], [4, 1, 3, 0, 10])
        [8, 4, 4, 1, 3, 0, 10]
    '''
                                                                                                            # PUT YOUR CODE HERE
    pass    # remove the 'pass'

# Question 2(a)

# v = np.array([1,3,5])

def bowl_cost(v):
    '''
        v is the price vector
        it can take any value like this: np.array([1,3,5])
        The store sells the following fruit bowls:
            #1: 3 of each fruit
            #2: 2 mangos and 8 apricots
            #3: 5 strawberries and 3 apricots
            #4: 10 apricots
        Create a 2-dimensional numpy array encoding the matrix B such that the matrix-vector multiplication
            B x v
        evaluates to a length 4 column vector containing the price of each fruit bowl. 
        The first entry of the result should be the cost of fruit bowl #1, the second entry the cost of fruit bowl #2, etc.
    '''

    B = np.array([
        [3, 3, 3],
        [2, 0 ,8],
        [0, 5, 3],
        [0, 0, 10],
    ])
    # The notation B @ v means: compute the matrix multiplication Bv
    return B @ v

# bowl_cost(v)


# Question 2(b)
def amount_spent(v, B):
    '''
        v and B are from the previous question (2a).
        Bob, Daniela, and Luke make the following purchases:
        * Bob buys 2 fruit bowl #1's and 1 fruit bowl #3.
        * Daniela buys 1 of each fruit bowl.
        * Luke buys 10 fruit bowl #4s (he really likes apricots).
        Create a matrix A such that the matrix expression
            A x B x v
        evaluates to a length 3 column vector containing how much each of them spent. 
        The first entry of the result should be the total amount spent by Bob, the second entry the amount sent by Daniela, etc.
    '''

    A = np.array([
        [2, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 10],
    ]) 
    
    return A @ B @ v 


# Question 2(c)

from numpy.linalg import inv

def new_price(A, B, x):
    '''
        A and B are from previous question (2b).
        Let's suppose Berkeley Bowl changes their fruit prices, but you don't know what they changed their prices to. 
        Joey, Deb, and Sam buy the same quantity of fruit baskets and the number of fruit in each basket is the same, 
        but now the amount they spent is given by 'x':
        Use np.linalg.inv and x to compute the new prices for the individual fruits:
    '''

    fruit = A @ B
    fruit_inv = inv(fruit)
    new_v = fruit_inv @ x
    return new_v

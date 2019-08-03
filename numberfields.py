# ---------------------------------------------------------------------------
#                       Elementary Number Theory
# ---------------------------------------------------------------------------

# List primes less than an upper-bound.
def sieve_eratosthenes(n):


    '''
        Input: Integer (type, int)
        Output: all primes less than input intger (type, list)

    '''

    # Inititally the sieve contains all numbers less than n.
    primes = range(2,n)

    # Now we remove multiples and iterate. We sieve out the composites.
    count = 0

    while count <  len(primes):
        for x in primes:
            if primes[count] == x:
                pass
            elif (x % primes[count] == 0):
                primes.remove(x)
            else:
                pass
        count += 1
    return primes

# Number of primes less than an upper-bound.
def landau_primecount(n):

    '''
        Input: Integer (type, int)
        Output: number of primes less than or equal to the input integer
        (type, int)

        Slow by n = 100,000.

    '''

    primes = sieve_eratosthenes(n+1)
    return len(primes)

# The functions above calculate a bunch of prime numbers. The next function
# takes an integer as input and returns (Boolean) whether or not it is prime.
# In order to check whether an integer is prime, it suffices to check for
# divisors upto and including it's squareroot.

# Newton-Raphson is used to calculate (approximate) the squareroot.
def newton_sqrt(x):

    '''
        Input: a number (Type, int or float) whose squareroot is sought
        Output: Squareroot of input (Type, float)

        Squareroot is approximated using Newton-Raphson.

    '''

    x_initial = 1
    # Delta is the difference between iterations. Used to say how accurate
    # we want the squareroot.
    delta = 1

    while delta > 0.001:
        x_new = x_initial - ( ((x_initial ** 2) - x ) / float((2 * x_initial)))
        delta = abs(x_new - x_initial)
        x_initial = x_new

    return x_initial

# Now that we can calculate squareroots, we can write a primality test.
def isit_prime(n):

    '''
        Input: an integer (Type, int)
        Output: whether or not input is prime (Type, Boolean)

        This function tests divisiblity for each integer upto the squareroot
        of the input.

        Time taken to execute noticeable near the prime n = 1000000000039

    '''
    # We need only test divisiblity upto and including squareroot.
    divisor_bound = int(newton_sqrt(n))+1
    # Boolean which will stop loop if divisor found.
    has_divisor = False

    d = 3
    while d <= divisor_bound:
        if (n % d) == 0:
            has_divisor = True
            break
        else:
            d = d + 2

    if (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    elif n == 1:
        return False
    elif has_divisor == True:
        return False
    else:
        return True

# Now that we can detect primes, we can begin to calculate the prime
# factorisation of an integer. For this we will need:
#               (i) Detect divisors
#              (ii) Calculate highest powers of divisors

def exponent_of_divisor(n,d):

    '''
        Input: Integers (Type, int).
        Output: (Type, int)

        This function returns the highest power of d that divides n.

    '''

    count = 0

    while ((n%d)==0):
        n = n/d
        count +=1

    return count

def isit_divisor(n,d):

    '''
        Input: Two (Type, integers)
        Output: True or False (Type, Boolean)

        Output True if d divides n, False otherwise.
    '''

    if d == 0:
        return False
    elif (n%d) == 0:
        return True
    else:
        return False

def divisors(n):

    '''
        Input: Integer (Type, int)
        Output: List of integers (Type, list)

        Output is the list of divisors of the input n.

    '''

    divisors = [1,n]

    for i in range(2,int(newton_sqrt(n)+1)):

        if (n%i) == 0:
            divisors.append(i)
            if not (i == n/i):
                divisors.append(n/i)
            else:
                pass
        else:
            pass

    return divisors

def prime_divisors(n):

    ''' Input: Integer (Type, int) whose prime divisors are sought
        Output: List (Type, list) of prime divisors
    '''

    divisors_list = divisors(n)
    prime_divisors = []
    for d in divisors_list:
        if isit_prime(d) == True:
            prime_divisors.append(d)
        else:
            pass

    return prime_divisors

def prime_factorisation(n):

    '''
        Input: Integer (Type, integer) whose prime factorisation is sought.
        Output: Prime factorisation (Type, str) of input integer.


        Okay upto n = 3000235347293732ish (Quadrillions = 1000s of Trillion)
        It takes, approximately, 17 seconds to factor the following integer.
            Example: Prime factorisation of 3 Quadrillion ...
        3000235347293732 = 2^2 x 31 x 137 x 42643 x 4141573

        Another factor of 10 yields a memory error on my laptop.

    '''

    prime_divisor_list = prime_divisors(n)
    exponents = []
    for i in prime_divisor_list:
        exponents.append(exponent_of_divisor(n,i))

    prime_factorisation = ''
    for i,j in zip(prime_divisor_list,exponents):
        prime_factorisation += ('%s^%s x ' % (str(i),str(j)))

    print '\n'
    return ('%s = ' % str(n)) + prime_factorisation[:-3]

# ---------------------
#  Euclidean Algorithm
# ---------------------

# This is an ancient algorithm for determining the "greatest common divisor"
# i.e. GCD of two positive integers.
def euclid_gcd(a,b):

    '''
        This function implements the ancient algorithm of Euclid in order
        to determine the greatest common divisor (gcd) of two integers.

        Input: integers a,b
        Output: greatest common divisor of a,b (type integer)

    '''

    r = (a%b)

    if r == 0:
        return b
    else:
        a = b
        b = r
        return euclid_gcd(a,b)

# With this function we can define Euler's totient (phi) function.
def euler_totient(n):

    '''
        Input: An integer (Type, int)
        Output: Number of integers less than that are coprime to n (Type, int)

        Note: this assumes input is greater than 1.

    '''

    count = 1
    # Increase count by 1 each time an integer is coprime to n.
    for x in range(2,n):
        if euclid_gcd(x,n) == 1:
            count +=1
        else:
            pass

    return count

# Extended Euclidean algorithm allows us to calculate inverses in modular
# arithmetic, when they exist.
def extended_euclid_gcd(a,b):

    '''
        Input: Integers m,n (Type, int)
        Output: Integers a,b such that am + bn = gcd(m,n) (Type, int)

    '''

    # Initialize the outputs.
    s = 0           # s (old_s) will be the multiple of a.
    old_s = 1
    t = 1           # t (old_t) will be the multiple of b.
    old_t = 0
    r = b           # r (old_r) will be the greatest common divisor.
    old_r = a

    while (not (r == 0)):
        q = old_r / r
        (old_r,r) = (r, old_r - q*r)
        (old_s,s) = (s, old_s - q*s)
        (old_t,t) = (t, old_t - q*t)


    print "Bezout coefficients: ", (old_s, old_t)
    print "[%s]*%s + [%s]*%s = gcd(%s,%s) = %s" % (old_s,a,old_t,b,a,b,old_r)
    print "Greatest common divisor: ", old_r
    return "What more could you want?"

# ... with the extended Euclidean algorithm implemented we can now calculate
# inverses in modular arithmetic.
def euclid_modular_inverse(a,p):

    '''
        Input: Integers a,p (Type, int)
        Output: Inverse of a mod p. (Type, int).

        Note: This code assumes a < p and that the inverse exists. Not the
        function will return "None" if a is not invertible mod p.

        Note: This function employs the extended Euclidean algorithm to find
        the gcd and inverse.

        Note: This function assuemes neither input is 0.


    '''

    # Initialize the outputs.
    s = 0
    old_s = 1       # old_s will be the inverse of a.
    t = 1
    old_t = 0
    r = p
    old_r = a       # old_r is the greatest common divisor of a,p

    while (not (r == 0)):
        q = old_r / r
        (old_r,r) = (r, old_r - q*r)
        (old_s,s) = (s, old_s - q*s)
        (old_t,t) = (t, old_t - q*t)

    # We want a representative for the inverse of a in [0,p-1]. In the case
    # that old_s is negative, we have to add p to it in order to get a positive
    # representative for the coset.
    if old_s < 0:
        old_s += p
    else:
        pass

    # Return value depends on whether a is invertible.
    if old_r == 1:
        return old_s
    else:
        print "%s not invertible mod %s" % (a,p)
        return None

# ---------------------------------------------------------------------------
#                         Algebraic Number Theory
# ---------------------------------------------------------------------------

class Numberfield:


    '''
        Objects of this class are numberfields i.e. finite extensions
        of the rational numbers. These will be specified by the irreducible
        separable polynomial that generates them.

    '''

    def __init__(self,polynomial):

        '''
            In order to specify a numberfield we will require a polynomial.
            These are to be entered as lists of coefficients. In order to
            get the index of the list to match the coefficient of the
            polynomial we will have the highest degree term to be the
            last element of the list.

            Example: x^2 + 2x + 3 = [3,2,1]

            This means that the length of the polynomial is always one more
            than the degree.

        '''

        self.polynomial = polynomial

    def degree(self):

        '''
            This function returns the degree of the extension defined by the
            object. Recall the list representation is one longer than the
            degree of the polynomial.

        '''

        return len(self.polynomial)-1

    def discriminant(self):

        '''
            This function returns the discriminant of the polynomial
            that generates the extension.

        '''

        if self.degree() == 2:
            a = self.polynomial[2]
            b = self.polynomial[1]
            c = self.polynomial[0]
            return (b**2) - 4*a*c
        else:
            return "I can't do that yet."

    def ramifiedprimes(self):

        '''
            This returns the list primes that ramify in the numberfield.
            This uses the fact that the primes which ramify in a numberfield
            are precisely the primes that divide the discriminant.

        '''

        # For some reason this prints two twice when disc = p^2
        return prime_divisors( abs(self.discriminant()))
    

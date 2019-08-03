# Finite Field Arithmetic

class FiniteField:


    '''
        Objects of this class are finite fields specified by:

          (i) characteristic (i.e. a prime number)
         (ii) their degree
        (iii) irreducible polynomial

        Polynomials are represented as lists. The index of the list
        corresponds to the degree of the term in the polynomial.

    '''


    def __init__(self, char, irredpoly):

        # If the input polynomial is NOT irreducible modulo the characteristic
        # specified at the creation of the instance, then we should raise
        # an error. If no error is raised, then the instance can be created.


        self.char = char
        self.poly = irredpoly
        self.degree = len(irredpoly)-1      # Subtract 1 on account of the
                                            # length being longer than the
                                            # the degree.
        self.num_of_elem = (self.char ** self.degree)

# Some examples of finite fields.
gf2_2 = FiniteField(2,[1,1,1])
gf3_2 = FiniteField(3,[1,0,1])

class FiniteFieldElem:

    '''
        Instances of this class are elements in some finite field. In order
        to specifiy an element of this class one has to say: which field it
        is in and what the coefficients of the polynomial are they define
        this element.

    '''

    def __init__(self, field, coefficients):
        self.coef = coefficients
        self.field = field

    def in_field(self):

        '''
            Prints a string which says which field the element is in.
            Uses the "Galois Field" notation.

            For example: the unique extension of degree 3 over F3 is denoted
                         GF(27)

        '''
        degree = (self.field).degree
        char = (self.field).char

        return 'GF(%s)' % (char**degree)

    def polynomial(self):

        '''
            This function prints the element of a finite field as a polynomial.

        '''

        count = 0
        polynomial = ''
        for x in self.coef:
            polynomial += ('(%d t ^ %d)+' % (x,count))
            count += 1
        return polynomial[:-1]

    # We want to be able to do some arithmetic in these fields. These can
    # be implemented using static methods.

    @staticmethod
    def add(z,w):

        '''
            This static method takes two elements in a finite field and
            returns the sum of those elements in that field.

        '''

        if not z.field == w.field:
            raise NameError("These elements don't belong to the same field.")
        else:
            add = [(sum(x) % (z.field).char) for x in zip(z.coef,w.coef)]
            return FiniteFieldElem(z.field,add)

w = FiniteFieldElem(gf2_2,[0,1])
x = FiniteFieldElem(gf3_2,[1,1])
z = FiniteFieldElem(gf2_2,[1,1])

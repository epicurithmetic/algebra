#                               Complex numbers
class Complex:

    '''
        Instances of this class are complex numbers. We specify an instance
        by giving the real and imaginary parts.

        For example: z = 3+2i is defined as z = Complex(3,2)

    '''

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def cartesian(self):

        '''
            This method prints an imaginary number as a string.
            The representation is in Cartesian coordinates.

        '''
        return "%d + %di" % (self.real, self.imaginary)

    def conjugate(self):

        '''
            This function returns the complex conjugate of the input.
            For example: 3 + 2i is sent to 3 - 2i

        '''

        return Complex(self.real, -self.imaginary)


    # These methods don't refer to "self" as they are functions which
    # take multiple instances of the Complex class as inputs. As such
    # I have designated them as static methods.
    @staticmethod
    def add(z,w):
        return Complex((z.real+w.real),(z.imaginary+w.imaginary))

    @staticmethod
    def mult(z,w):
        real_part = (z.real*w.real - z.imaginary*w.imaginary)
        imaginary_part = (z.real*w.imaginary + z.imaginary*w.real)
        return Complex(real_part,imaginary_part)

x = Complex(0,1)
y = Complex(0,2)

print Complex.cartesian(Complex.add(x,y))
print Complex.cartesian(Complex.conjugate(x))

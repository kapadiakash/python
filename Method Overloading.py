

# class Calculator:
#     def add(self,a,b,c=None):
#         if c is not None:
#             return a + b + c
#         else:
#             return a + b
# a = Calculator()
# b = a.add(2,3)
# b1 = a.add(2,3,4)


class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

# Usage
calc = Calculator()
result1 = calc.add(2, 3)       # Calls the version with two parameters
result2 = calc.add(2, 3, 4)    # Calls the version with three parameters
Calculator()
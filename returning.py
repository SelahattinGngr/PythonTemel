def usalma(number):
      
    def inner(power):
         return number ** power

    return inner

two = usalma(2)
print(two(3))
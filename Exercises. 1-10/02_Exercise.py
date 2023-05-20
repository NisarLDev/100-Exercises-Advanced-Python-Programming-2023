# My solution

def calculate():
    numeroprevio=1
    numeroactual=2
    sumatotal=0   
    while numeroactual<=1000000:
        if numeroactual%2==0:
            sumatotal+=numeroactual
        temporal=numeroactual
        numeroactual=numeroactual+numeroprevio
        numeroprevio=temporal
    return  sumatotal
    
print(calculate())

# Solution of the instructor
  
   
   
      def calculate():
        total = 0
        a = 0
        b = 1
        while a < 1000000:
            if a % 2 == 0:
                total += a
            a, b = b, a + b
        return total
     
     
    print(calculate())
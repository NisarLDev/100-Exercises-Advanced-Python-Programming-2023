# My solution



# Solution of the instructor
  
   
   
    def calculate():
        numbers = []
        for i in range(100):
            if i % 5 == 0 or i % 7 == 0:
                numbers.append(i)
        total = sum(numbers)
        return total
     
     
    print(calculate())

    # OR

        def calculate():
        return sum([i for i in range(100) if i % 5 == 0 or i % 7 == 0])
     
     
    print(calculate())
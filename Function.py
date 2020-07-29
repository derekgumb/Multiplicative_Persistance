def mult_persistence(n):
    done_with_persistence = False
    accum = 0

    def find_int_length(my_int):
        #Find number of digits in num
        return len(str(my_int))

    def mult(my_int):
        #Funct that finds product of digits in a num multiplied together
        res = 1
        for i in range(len(str(my_int))):
            res = res * int(str(my_int)[i])
        return res

    while not done_with_persistence:
        #Success if product of mult persistence is a 1-digit number
        if find_int_length(n) == 1:
            done_with_persistence = True
        #Continue mult persistence if product has 2-digits or more
        elif find_int_length(n) >= 2:
            if find_int_length(mult(n))==1:
                accum+=1
                done_with_persistence = True
            elif find_int_length(mult(n))>=2:
                accum+=1
                n = mult(n)
                continue

    return accum
            
print(mult_persistence(999))
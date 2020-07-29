def mult_persistence(n):
    done_with_persistence = False
    accum = 0

    #Finds number of digits in n:
    def find_int_length(my_int):
        return len(str(my_int))

    #Finds product of digits in n multiplied together:
    def mult(my_int):
        res = 1
        for i in range(len(str(my_int))):
            res = res * int(str(my_int)[i])
        return res

    while not done_with_persistence:
        #Conclusion of program if n is a 1-digit number:
        if find_int_length(n) == 1:
            done_with_persistence = True
        #Continue mult persistence if n has 2-digits or more:
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

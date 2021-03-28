def ascending(n):
    #takes the first digit of the number
    m = int(str(n)[:1]) 
    #finds the first value of the list
    current_digit = int(str(n)[1 : 1 + m])
    #creates the list
    list_for_numbers = [current_digit]
    #takes away first digit and first number from the input
    n = int(str(n)[1 + m:])
    #reverses the number
    n = int(str(n)[::-1])
    #placeholder for other values
    placeholder = 0
    #digit to find how long each value is going to be
    reset = 1

    #makes it so you won't go over the limit, knows when to stop
    while len(str(n)) - reset >= 0:
        #takes the numbers one by one
        placeholder = int(str(n)[ : reset])
        
        #checks if theres not enough space
        if reset > len(str(n)):
            return list_for_numbers

        #checks if number meets requirement
        elif placeholder > current_digit:
            #adds number to list
            list_for_numbers.append(placeholder)
            #turns current number to placeholder
            current_digit = placeholder
            #if that was the last possible value it will return
            if current_digit == n:
                return list_for_numbers
            #removes the value from the original number
            else:
                n = int(str(n)[reset:])
            #resets reset
            reset = 0
        #adds one to reset because python can't handle 0
        reset += 1
        
    return list_for_numbers
    

print(ascending(412342987656784352))
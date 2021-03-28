def fibbonacci(n):
    if n == 1 or n == 2:
        return 1

    old_num = 1
    new_num = 1
    
    for i in range (n - 2):
        
        current_num = old_num + new_num
        old_num = new_num
        new_num = current_num
        
    return current_num

print(fibbonacci(2))
    
    
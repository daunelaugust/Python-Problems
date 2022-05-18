def dont_give_me_five(start,end):
    # your code here
    
    n = len([i for i in range(start,end+1) if '5' not in str(i)])
  
        
    return n   # amount of numbers
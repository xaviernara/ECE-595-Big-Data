userWithdrawl = int(input("Enter the amount for withdrawal: "));

if userWithdrawl % 5 == 0:
    
    # check to see if we can withdraw 100
    hundreds = userWithdrawl // 100
    if hundreds:
        #print(f"100: {hundreds}")
        print("$100:", hundreds) # this does the same thing as the above line
        
        # minus the 100's from the amount
        userWithdrawl -= hundreds * 100
        
    fifties = userWithdrawl // 50
    if fifties:
        print("$50:", fifties)
        userWithdrawl -= fifties * 50
        
    twenties = userWithdrawl // 20
    if twenties:
        print("$20:", twenties)
        userWithdrawl -= twenties * 20
        
    fives = userWithdrawl // 5
    if fives:
        print("$5:", fives)
        
   
   
if userWithdrawl % 5 != 0:  
   #divisibleByFive = False;
   print ("The amount ", userWithdrawl , "cannot be withdrawn." );



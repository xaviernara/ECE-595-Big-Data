#Floor Division(//): Divides and returns the integer value of the quotient. 
#It dumps the digits after the decimal.
#Ex:3/4 =0.75
#Ex:3//4 =0
#Ex:4/3 =1.33
#Ex:4//3 =1


userWithdrawl = int(input("Enter the amount for withdrawal: "));

#dispenes hundread dollar bills
def hundredDispense(num):
#if the remainder of the amount is divisble by 50,20,10, or 5 after its been divided by 100 
#then its sent to the corresponding function that dispenses that amount
#EX:150/100 = 1 R 50

   hundredDispensing= int(num/100);
   print ("$100:",hundredDispensing);
   remainder = num%100
   
   if num % 50 == 0:
     fiftyDispense(num=remainder);
     
   elif num % 20 == 0:
      twentyDispense(num=remainder);
    
   elif num % 10 == 0:
      tenDispense(num=remainder);

   elif num % 5 == 0:
      twentyDispense(num=remainder);
   else:
         print("Transaction complete.")
         
    

#dispenes fifty dollar bills
def fiftyDispense(num):
#if the remainder of the amount is divisble by 20,10, or 5 after its been divided by 50 
#then its sent to the corresponding function that dispenses that amount
#EX:55/50 = 1 R 5

   fiftyDispensing= int(num/50);
   print ("$50:",fiftyDispensing);
   remainder = num%50
   
   if num % 20 == 0:
      twentyDispense(num=remainder);
          
   elif num % 10 == 0:
      tenDispense(num=remainder);
      
   elif num % 5 == 0:
      twentyDispense(num=remainder);
   else:
       print("Transaction complete.")
       


#dispenes twenty dollar bills      
def twentyDispense(num):
#if the remainder of the amount is divisble by 10 or 5 after its been divided by 20 
#then its sent to the corresponding function that dispenses that amount
#EX:45/20 = 2 R 5

   twentyDispensing= int(num/20);
   print ("$20:",twentyDispensing);
   remainder = num%20
   
   if num % 10 == 0:
      tenDispense(num=remainder);
              
   elif num % 5 == 0:
      twentyDispense(num=remainder);
   else:
       print("Transaction complete.")
      

#dispenes 10 dollar bills
def tenDispense(num):
#if the remainder of the amount is divisble by 5 after its been divided by 10 
#then its sent to the corresponding function that dispenses that amount
#EX:15/10 = 1 R 5

   tenDispensing= int(num/10);
   print ("$10:",tenDispensing);
   remainder = num%10
   
   if num % 5 == 0:
      fiveDispense(num=remainder);
   else:
         print("Transaction complete.")
        

#dispenes five dollar bills
def fiveDispense(num):
#if the remainder of the amount is still divisble by 5 after its been divided by the previous functions  
#then its dispenses that amount in 5's
#EX:15/10 = 1 R 5

   fiveDispensing= int(num/5);
   print ("$5:",fiveDispensing);
   print("Transaction complete.");
   
   


divisibleByFive = bool(True);
# n%k==0 evaluates true if and only if n is an exact multiple of k. 
#In elementary maths this is known as the remainder from a division.
if userWithdrawl % 5 == 0:
   print("Please collect your bills as follows:");

else:  
   divisibleByFive = False;
   print ("The amount ", userWithdrawl , "cannot be withdrawn." );


   



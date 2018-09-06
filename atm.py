#Floor Division(//): Divides and returns the integer value of the quotient. 
#It dumps the digits after the decimal.
#Ex:3/4 =0.75
#Ex:3//4 =0
#Ex:4/3 =1.33
#Ex:4//3 =1


userWithdrawl = int(input("Enter the amount for withdrawal: "));
#remainder = 0 

#dispenes hundread dollar bills
def hundredDispense(num):

   hundredDispensing= int(num/100);
   print ("$100:",hundredDispensing);
   remainder = num%100
   
   if num % 50 == 0:
     #print("1st remainder: ",remainder);
     fiftyDispense(num=remainder);
     
   elif num % 20 == 0:
      #print("2nd remainder: ",remainder);
      twentyDispense(num=remainder);
    
   elif num % 10 == 0:
      #print("2nd remainder: ",remainder);
      tenDispense(num=remainder);

   elif num % 5 == 0:
      #print("2nd remainder: ",remainder);
      twentyDispense(num=remainder);
   else:
         print("Transaction complete.")
         break
    

#dispenes fifty dollar bills
def fiftyDispense(num):

   fiftyDispensing= int(num/50);
   print ("$50:",fiftyDispensing);
   remainder = num%50
   
   if num % 20 == 0:
      #print("2nd remainder: ",remainder);
      twentyDispense(num=remainder);
          
   elif num % 10 == 0:
      #print("2nd remainder: ",remainder);
      tenDispense(num=remainder);
      
   elif num % 5 == 0:
      #print("2nd remainder: ",remainder);
      twentyDispense(num=remainder);
   else:
       print("Transaction complete.")
       break


#dispenes twenty dollar bills      
def twentyDispense(num):

   twentyDispensing= int(num/20);
   print ("$20:",twentyDispensing);
   remainder = num%20
   
   if num % 10 == 0:
      #print("2nd remainder: ",remainder);
      tenDispense(num=remainder);
              
   if num % 5 == 0:
      #print("2nd remainder: ",remainder);
      twentyDispense(num=remainder);
   else:
       print("Transaction complete.")
       break

#dispenes 10 dollar bills
def tenDispense(num):

   tenDispensing= int(num/10);
   print ("$10:",tenDispensing);
   remainder = num%10
   
   if num % 5 == 0:
      #print("2nd remainder: ",remainder);
      fiveDispense(num=remainder);
   else:
         print("Transaction complete.")
         break

#dispenes five dollar bills
def fiveDispense(num):
   fiveDispensing= int(num/5);
   print ("$5:",fiveDispensing);
   print("Transaction complete.");
   break


divisibleByFive = bool(True);
# n%k==0 evaluates true if and only if n is an exact multiple of k. 
#In elementary maths this is known as the remainder from a division.
if userWithdrawl % 5 == 0:
   print("Please collect your bills as follows:");
   hundredDispense(num=userWithdrawl)

else:  
   divisibleByFive = False;
   print ("The amount ", userWithdrawl , "cannot be withdrawn." );


   
while divisibleByFive:
    if userWithdrawl % 100 == 0:
         hundreadDispense= int(userWithdrawl/100);
         remainder = userWithdrawl%100
         print ("$100:",hundreadDispense);
         print("remainder",remainder);
         break;
         
   
   
      #hundredmoneyback = userWithdrawl// hundred;
      #hundredpartialtotal = userWithdrawl - hundredmoneyback * hundred;
            
      #fiftymoneyback = hundredpartialtotal // fifty;
      #fiftypartialtotal = hundredpartialtotal - fiftymoneyback * fifty;
      
      #twentymoneyback = fiftypartialtotal // twenty;
      #twentypartialtotal = fiftypartialtotal - twentymoneyback * twenty;
      
      #tenmoneyback = twentypartialtotal // ten;
      #tenpartialtotal = twentypartialtotal - tenmoneyback * ten;
      
      #fivemoneyback = twentypartialtotal // five;
      #fivepartialtotal = twentypartialtotal - fivemoneyback * five;

      
      
      #print "$100: %s, $50: %s, $20: %s,  $10: %s,  $5: %s." % (hundredpartialtotal, fiftymoneyback, twentymoneyback,tenmoneyback,fivemoneyback)
      #print ("$100:",hundredpartialtotal);
      #print ("$50:",fiftymoneyback);
      #print("$20:",twentymoneyback);
      #print("$10:",tenmoneyback);
      #print(" $5:",fivemoneyback);
      
      #break;
        
else:  
   divisibleByFive = False;
   print ("The amount ", userWithdrawl , "cannot be withdrawn." );


#if userWithdrawl % 100 == 0:
#   print("100 divisible");

#elif userWithdrawl % 20 == 0:
#   print("20 divisible");


#print(userWithdrawl);

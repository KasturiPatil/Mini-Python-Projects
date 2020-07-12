while True:
      pin = int(input("Enter account pin:"))
      if pin > 1000 and pin < 9999:
            print("1-View Balance       2-Withdraw        3-Deposit         4-Exit")
            break
      else:
            print("Invalid Pin Entered.")

class Account:
      def __init__(self,balance = 0):
            self.balance = balance

      def ViewBalance(self):
            return self.balance

      def Withdraw(self):
            withdraw_amt = float(input("Enter amount to withdraw:"))
            
            if withdraw_amt < self.balance:
                  check= input("Is this the correct amount, Y/N?")
                  if check == "Y" or check =="y":
                        self.balance -= withdraw_amt
                        print("Remaining Balance:",obj.ViewBalance())
            else:
                  print("You're balance is less than withdrawl amount.")
                  print("Please make a deposit.")

      def Deposit(self):
            deposit_amt = float(input("Enter amount to deposit:"))
            
            check = input("Is this the correct amount, Y/N?")
            if check == "Y" or check =="y":
                  self.balance += deposit_amt
                  print("Updated Balance:", obj.ViewBalance())
            else:
                  pass
      
obj=Account()
while True:
            select = int(input("\nEnter your selection:"))
     
            if select==1:
                  print("Your current Balance is:",obj.ViewBalance())
                  
            elif select==2:
                  obj.Withdraw()
                  
            elif select == 3:
                  obj.Deposit()                
                  
            elif select == 4:
                  print("\nTransaction Successfull.")
                  print("Balance:", obj.ViewBalance())
                  
                  break
            
            else:
                  print("\nInvalid selection. Please select again")
                  


      
      
      

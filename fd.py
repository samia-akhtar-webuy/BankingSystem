
import math

class BankAccount:
    def __init__(self, accountNumber, name ):
        self.__accountNumber = accountNumber
        self.__name = name

    def get_account_number(self):
        return self.__accountNumber


    def get_name(self):
        return self.__name


    def set_account_number(self, value):
        self.__accountNumber = value


    def set_name(self, value):
        self.__name = value

class FixedDeposit(BankAccount):
    def __init__(self, accountNumber, name, duration, amount, rateOfInterest, interest ):
        super().__init__(accountNumber,name)
        self.__duration = duration
        self.__amount = amount
        self.__rateOfInterest = rateOfInterest
        self.__interest = interest

    def get_duration(self):
        return self.__duration


    def get_amount(self):
        return self.__amount


    def get_rate_of_interest(self):
        return self.__rateOfInterest


    def set_duration(self, value):
        self.__duration = value


    def set_amount(self, value):
        self.__amount = value


    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value

    def set_interest(self):
        self.__interest=0;
    
        
class RecurringDeposit(BankAccount):
    def __init__(self, accountNumber, name, duration, monthlyPayment, rateOfInterest,interest ):
        super().__init__(accountNumber,name)
        self.__duration = duration
        self.__monthlyPayment = monthlyPayment
        self.__rateOfInterest = rateOfInterest
        self.__interest = interest


    def get_duration(self):
        return self.__duration


    def get_monthly_payment(self):
        return self.__monthlyPayment


    def get_rate_of_interest(self):
        return self.__rateOfInterest


    def set_duration(self, value):
        self.__duration = value


    def set_monthly_payment(self, value):
        self.__monthlyPayment = value


    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value

    def set_interest(self):
        self.__interest=0;

class BankDemo:
    n=0
    ch='n'
    
    def bankOptions(self):
        while(1):
            print("\t\t\t************************************************")
            print("\t\t\t         WELCOME TO DEPOSIT SECTION                ")
            print("\t\t\t************************************************")
            print("\t\t\t\t1. FIXED DEPOSIT")
            print("\t\t\t\t2. RECURRING DEPOSIT")
            print("\t\t\t\t3. Exit")
            
            n=int(input("\nSelect your choice : "))
            if n==1:
                self.readWriteFixedDeposit()
            elif n==2:
                self.readWriteRecurringDeposit()
            elif n==3:
                print("Thank You for using our services!!!")
                break
            else:
                print("Invalid option!\n try again\n")
                self.bankOptions() 
    
    def readWriteFixedDeposit(self):        
        print("\nGive Fixed Deposit Details\n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Enter Account Number: ").strip())
                j=1
            except:
                print("Please try again")
        name =input("Enter Account Name: ").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duration: ").strip())
                j=1
            except:
                print("Please try again")
        j=0
        while(j==0):
            try:
                amount = float(input("Amount: ").strip())
                j=1
            except:
                print("Please try again")
        
        j=0
        while(j==0):
            try:
                if duration==1:
                    rateOfInterest = 3
                elif duration>1 and duration<=5:
                    rateOfInterest = 7
                elif duration>5 and duration<=10:
                    rateOfInterest = 10
                else:
                    rateOfInterest = 15
                
                interest = (amount*rateOfInterest*duration)/100 
                interest = interest+amount
                j=1
            except:
                print("Please try again")
               
       
        
        fd = FixedDeposit(accountNumber, name, duration, amount, rateOfInterest,interest)
        
        print("\nFixed Deposit Details are...\n")
        print("\nAccount Number: ", fd.get_account_number())
        print("Account Name: ", fd.get_name())   
        print("Duration: ", fd.get_duration())
        print("Amount: ", fd.get_amount())
        print("Rate of Interest: ", fd.get_rate_of_interest())
        print("Interest Earned: ",interest-amount)
        print("Final amount: ", interest)
        
    def readWriteRecurringDeposit(self):
        print("\nGive Recurring Deposit Details\n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Enter Account Number: ").strip())
                j=1
            except:
                print("Please try again")
        name =input("Enter Account Name: ").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duration in months: ").strip())
                j=1
            except:
                print("Please try again")
        j=0
        while(j==0):
            try:
                monthlyPayment = float(input("Monthly Payment: ").strip())
                j=1
            except:
                print("Please try again")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Rate of Interest: ").strip())
                t=1+(((duration+1)*rateOfInterest)/2400)
                interest=monthlyPayment*duration*t
                j=1
            except:
                print("Please try again")   
      
                
        rd = RecurringDeposit(accountNumber, name, duration, monthlyPayment, rateOfInterest,interest)
        
        print("\nRecurring Deposit Details are...\n")
        print("\nAccount Number: ", rd.get_account_number())
        print("Account Name: ", rd.get_name())   
        print("Duration: ", rd.get_duration())
        print("Monthly Payment: ", rd.get_monthly_payment())
        print("Rate of Interest: ", rd.get_rate_of_interest())
        print("Amount deposited: ",duration*monthlyPayment)
        print("Interest Earned: ",interest-(monthlyPayment*duration))
        print("Final amount: ", interest)
        
        
 
def main():
    
    demoObject = BankDemo()
    demoObject.bankOptions()
  

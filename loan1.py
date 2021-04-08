
import math
def home_loan(principal, years,name,age,address,gender):
    # percent annual interest
    interest = 8.20
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    print("Name:",name)
    print("Age:",age)
    print("Address:",address)
    print("Gender:",gender)
    sf = '''\
        For a {} year loan of Rs.{:,}
        at an annual interest rate of {:.2f}%
        you pay Rs.{:.2f} monthly'''
    print(sf.format(years, principal, interest, payment))
    return payment

def car_loan(principal, years,name,age,address,gender):
    # percent annual interest
    interest = 9.25
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    print("Name:",name)
    print("Age:",age)
    print("Address:",address)
    print("Gender:",gender)
    sf = '''\
        For a {} year loan of Rs.{:,}
        at an annual interest rate of {:.2f}%
        you pay Rs.{:.2f} monthly'''
    print(sf.format(years, principal, interest, payment))
    return payment


def education_loan(principal, years,name,age,address,gender):
    # percent annual interest
    interest = 9.85
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    print("Name:",name)
    print("Age:",age)
    print("Address:",address)
    print("Gender:",gender)
    sf = '''\
        For a {} year loan of Rs.{:,}
        at an annual interest rate of {:.2f}%
        you pay Rs.{:.2f} monthly'''
    print(sf.format(years, principal, interest, payment))
    return payment
def main():
    while(1):
        print("\t\t\t************************************************")
        print("\t\t\t            WELCOME TO LOAN SECTION               ")
        print("\t\t\t************************************************")
        print("\t\t\t\t1.Home Loan\n\t\t\t\t2.Education Loan\n\t\t\t\t3.Car Loan\n\t\t\t\t4.Exit\n")
        ch=int(input("Enter your choice:"))
        #customer details
        name=input("Enter your name:")
        age=int(input("Enter age:"))
        address=input("Enter address:")
        gender=input("Gender:")

        
        if (ch==1):
            # loan principal
            principal = int(input("Enter the amount you want to take"))
            # years to pay off loan
            years = int(input("enter no. of years for you want to take loan"))
            # calculate monthly payment amount
            monthly_payment=home_loan(principal,years,name,age,address,gender)
            # calculate total amount paid
            total_amount = monthly_payment * years * 12
            # show result ...
            # {:,} uses the comma as a thousands separator
            
            print('-'*40)
            print("Total amount paid will be Rs.{:,.2f}".format(total_amount))
            print('-'*40)
        elif (ch==2):
            # loan principal
            principal = int(input("Enter the amount you want to take"))
            # years to pay off loan
            years = int(input("enter no. of years for you want to take loan"))
            # calculate monthly payment amount
            monthly_payment=education_loan(principal,years,name,age,address,gender)
            # calculate total amount paid
            total_amount = monthly_payment * years * 12
            # show result ...
            # {:,} uses the comma as a thousands separator
           
            print('-'*40)
            print("Total amount paid will be Rs.{:,.2f}".format(total_amount))
            print('-'*40)
        elif (ch==3):
            # loan principal
            principal = int(input("Enter he amount you want to take"))

            # years to pay off loan
            years = int(input("enter no. of years for you want to take loan"))
            # calculate monthly payment amount
            monthly_payment=car_loan(principal,years,name,age,address,gender)
            # calculate total amount paid
            total_amount = monthly_payment * years * 12
            # show result ...
            # {:,} uses the comma as a thousands separator
            
            print('-'*40)
            print("Total amount paid will be Rs.{:,.2f}".format(total_amount))
            print('-'*40)
        elif (ch==4):
            print("\tThanks for using bank managemnt system")
            break
        else :
            print("Invalid choice")


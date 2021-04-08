import account
import fd
import loan1

def main():

    choice = 1

    while choice != 4:
        print("\t\t\t************************************************")
        print("\t\t\t            WELCOME TO MERA BANK                ")
        print("\t\t\t************************************************")
        print("\t\t\t\t1. BANKING SERVICES ")
        print("\t\t\t\t2. LOAN SERVICES ")
        print("\t\t\t\t3. OTHER DEPOSITS ")
        print("\t\t\t\t4. QUIT ")

        try:
            choice = int(input())

        except:
            print("Invalid Choice")
            choice = 1
            continue

        if choice == 1:
            account.main();

        elif choice == 2:
            loan1.main();

        elif choice == 3:
            fd.main();

        elif choice == 4:
            print("Application Closed")

        else:
            print("Invalid Choice")

main()

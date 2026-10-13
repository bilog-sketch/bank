bal = 0
pin = 123
pintry = 3


while pintry > 0:
    enterpin = int(input("Enter PIN : "))
    if enterpin == pin:
    

    
        while True:
            print("ATM MACHINE")
            print("1 check balance")
            print("2 deposit")
            print("3 withdraw")
            print("4 transfer")
            print("5 Exit")

            choice = input("Enter here: ")

            if choice in ("1","2","3","4","5",):
                if choice == "1":
                    print(f"balance is {bal}")

                if choice == "2":
                    depo = int(input("Enter deposit amout : "))
                    if depo <= 0:
                        print("Enter positive")
                    else:
                        bal = bal + depo
                        print(f"you deposite {depo}")
                        print(f"balance now is: {bal}")

                if choice == "3":
                    withD = int(input("Enter withdraw amout: "))
                    if withD < 0:
                        print("Enter positive")

                    elif withD > bal:                       
                        print("kulang ung balance")

                    else:
                        if withD >= 5000:                     
                            tax = 10
                        else:
                            tax = 0

                        withDchecker = withD + tax

                        if withDchecker < bal:
                            bal = bal - withDchecker
                            print(f"you withdraw {withD}")
                            print(f"withdraw fee is {tax}")
                            print(f"balance now is: {bal}")
                        else:
                            print(f"kulang ang balance kaya di withdraw kasama ang tax")



                if choice == "4":
                    tran = int(input("Enter transfer amout: "))
                    if tran < 0:
                        print("Enter positive")

                    elif tran > bal:                       
                        print("kulang ung balance")

                    else:
                    
                        if tran >= 2000:
                        

                            tax = 20
                        else:
                            tax = 0

                        tranchecker = tran + tax
                    
                        
                        if checker <= bal:          
                            bal = bal - checker
                            print(f"you transferred: {tran}")
                            print(f"you transferedd succesfully")
                            print(f"Transfer fee is: {tax}")
                            print(f"balance left: {bal}")
                        else:
                            print("kulang ang ang balance ")
                         
    

                if choice == "5":
                    print("Bye ATM")
                    break
            else:
                print("wala sa pagpipilian")

        
    else:
    
        pintry = pintry - 1
        print(f"mali boy try left: {pintry}")
if pintry == 0:
    print("ATM LOCKED")
    

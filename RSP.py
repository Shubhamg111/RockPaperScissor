import random
choices = ['r','s','p']

u_choice = ""

while u_choice != "stop":
    u_choice = input("Enter Your Choice: ").lower()
    if u_choice == "stop":
        print("Game Over")
        break


    c_choice = random.choice(choices)
    
    if u_choice in choices:
        print("You choose ",u_choice)
        print("Computer choose ",c_choice)


        if c_choice == u_choice:
            print("tie")
            print("==============================")

        elif c_choice=="r" and u_choice=="s":
            print("Computer Wins")
            print("==============================")

        elif c_choice=="s" and u_choice=="p":
            print("Computer Wins")
            print("==============================")

        elif c_choice=="p" and u_choice=="r":
            print("Computer Wins")
            print("==============================")

        else:
            print("You Win")
            print("==============================")


    else:
        print("Invalid Input.")
        

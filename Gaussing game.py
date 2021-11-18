import random

c_guess = random.randint(1,3)
play_again = True
wallet = 0
reward = 0


while play_again:


    if wallet >= 10:
        wallet-=10

        for chance in range(1,4):
            print("chance: ",chance,"out of 3")

            u_guess = int(input("Enter the guesss :- "))
            if c_guess == u_guess:
                print("Congratulations !")
                if chance == 1:
                    print("You have won Rs.100 reward")
                    wallet = wallet + 100
                elif chance == 2:
                    print("You have won Rs.50 reward")
                    wallet = wallet + 50
                else:
                    print("You have won Rs.25 reward")
                    wallet = wallet + 25
                break
            else:
                print("Sorry Try Again !")
                if c_guess > u_guess :
                    print("you think of a bigger number")
                else:
                    print("you think of a smaller number")


        print("Your wallet has {} rs".format(wallet))

        choice = input("Do you want to play again [Yes/No]:- ")


        if choice != 'y':
            play_again = False

            withdraw = input ("Do want to withdraw your amount[Yes/No]:- ")
            if withdraw== 'y':
                w_amount = int(input("How much amount you want to withdraw :-Rs   "))
                if w_amount <= wallet:
                    wallet -= w_amount
                    print(f"The {w_amount} rs is transferred to your account ...! ")
                    print(f"your remaining balance is {wallet} Rs....!")
                else:
                    print("your wallet has insufficient funds ....!")

    else:
        print("Insufficient amount")
        amt = int(input("Enter min amount of Rs.10 : "))
        wallet += amt



































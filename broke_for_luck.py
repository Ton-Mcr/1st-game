import random
import sys
import time
# global variables
class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style_text(code):
        return "\33[{code}m".format(code=code)
  
    def color_text(code):
        return "\33[{code}m".format(code=code)

name= ""
i = 1
result = ""
attempts1 = 0
wallet = 100                #these are similar to functions but they are set code so insted of it being a program its like information stored
player_total = 0
dealer_total = 0


def print_slow(str):         #Def is where you define perameters around a funtion
    for letter in str:
        sys.stdout.write(letter)    #print slow is the function and here is the code to make the slow print
        sys.stdout.flush()
        time.sleep(0.02)


def roulette():
    print_slow(f"""
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$ Welcome {name} To Roulette $$$
    $$$ Please Gamble Responsably  $$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)
    global wallet 
    while wallet >1:
        try:
            bet_size = int(input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "How Much Would You Like To Bet ")) 
            if bet_size > wallet:
                print_slow ('"You dont have enough funds for that bet"\n')
                print_slow(f'"You Have {wallet} in your wallet"\n')    
            elif bet_size <= wallet: 
                wallet -= bet_size     
                print_slow(f'"You now Have {wallet} in your wallet"\n')
                print_slow('"Get ready to place your bets "\n')
                try:
                    numnum =int( input ("Place your bets now"' select number '  ))
                    random_number = random.randint(0, 36)
                    if numnum < 0 or numnum > 36:
                        print_slow ("That Number does not exist in roulette!")
                        wallet += bet_size
                        print_slow(f'"You Have {wallet} in your wallet"\n')
                    else:
                        if random_number == numnum:
                            print_slow ("Congratulations You have won ")
                            wallet += bet_size * 36
                            print(f"you now have {wallet} in your wallet")
                        else:
                            print_slow(f'"{random_number} House Wins, Next Bet"\n')
                except ValueError: 
                    print_slow ("That is not a number\n")
                    wallet += bet_size
                    print_slow(f'"You Have {wallet} in your wallet"\n')
            else:
                print_slow('"Invalid Input"\n')
                roulette()
        except ValueError as ve:
            print_slow('"Invalid Input"\n')
            roulette()
    if wallet ==0:
             print_slow (' "Oh, It seems You have no more money sir, please exit the table"\n'
         '\n'
         '\n'
         '\n'
         '\n'
         'You notice that 3 suspicious lookin men walk on to the Casino Floor,\n Stand by the ATM...\n They look like they are expecting you...\n They are Waiting for you\n ')     
    (input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  'Would you like to proceed to the ATM Y/N? '))



def slots():
    global wallet
    while wallet > 1:
        try:
            bet_size = int(input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "how much would you like to bet? "))
            if bet_size <= wallet:
                wallet -= bet_size
                print(f"you now have {wallet} in your wallet")
                winning_no1 = random.randint(1,10)
                winning_no2 = random.randint(1,10)
                winning_no3 = random.randint(1,10)
                if winning_no1 == winning_no2 and winning_no3 == winning_no1:
                    jackpot()
                    print("you win")
                    wallet += bet_size * 10
                    print(f"you now have {wallet} in your wallet")
                elif winning_no1 == winning_no2 and winning_no3 != winning_no1:
                    print("you win")
                    wallet += bet_size * 3
                    print(f"you now have {wallet} in your wallet")
                else:
                    print("you lose")
                    print(f"you now have {wallet} in your wallet")
            elif bet_size > wallet:
                print("you dont have enough funds for that bet")
                print(f"you have {wallet} in your wallet")
            else:
                print("invalid input")
                slots()
        except ValueError as ve:
            print("invalid input")
            slots()

def blackjack():
    global player_total, dealer_total, wallet
    while wallet > 1:
        try:
            bet_size = int(input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "how much would you like to bet? "))
            if bet_size <= wallet:
                wallet -= bet_size
                print(f"you now have {wallet} in your wallet")
                player_card1 = random.randint(1,11)
                player_card2 = random.randint(1,11)
                player_total = player_card1 + player_card2
                print(f"you have been dealt {player_card1} and {player_card2}")
                print(f"your total is {player_total}")
                dealer_card1 = random.randint(1,11)
                dealer_card2 = random.randint(1,11)
                dealer_total = dealer_card1 + dealer_card2
                print(f"the dealer has been dealt {dealer_card1} and {dealer_card2}")
                print(f"the dealers total is {dealer_total}")
                if player_total <= 21:
                    hit_or_stay = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "would you like to hit or stay? ")
                    def hitorstay():
                        if hit_or_stay.capitalize() == "Hit" or hit_or_stay.capitalize() == "H":
                            def player_hit():
                                global player_total, dealer_total, wallet
                                player_cardaddition = random.randint(1,11)
                                print(f"you have been dealt {player_cardaddition}")
                                player_total += player_cardaddition
                                if player_total < 21:
                                    def hitorstay2():
                                        print(f"your total is {player_total}")
                                        hit_or_stay = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "would you like to hit or stay? ")
                                        if hit_or_stay.capitalize() == "Hit" or hit_or_stay.capitalize() == "H":
                                            player_hit()
                                        elif hit_or_stay.capitalize() == "Stay" or hit_or_stay.capitalize() == "S":
                                            if dealer_total < 17:
                                                def dealer_hit():
                                                    global player_total, dealer_total, wallet
                                                    dealer_cardaddition = random.randint(1,11)
                                                    print(f"the dealer has been dealt {dealer_cardaddition}")
                                                    dealer_total += dealer_cardaddition
                                                    if dealer_total < 17:
                                                        dealer_hit()
                                                    elif dealer_total > 21:
                                                        print("the dealer busts")
                                                        wallet += bet_size * 2
                                                        print(f"you now have {wallet} in your wallet")
                                                        blackjack()
                                                    elif dealer_total > player_total:
                                                        print("the dealer wins")
                                                        blackjack()
                                                    elif dealer_total < player_total:
                                                        print("you win")
                                                        wallet += bet_size * 2
                                                        print(f"you now have {wallet} in your wallet")
                                                        blackjack()
                                                dealer_hit()
                                            elif dealer_total > 21:
                                                print("the dealer busts")
                                                wallet += bet_size * 2
                                                print(f"you now have {wallet} in your wallet")
                                                blackjack()
                                            elif dealer_total > player_total:
                                                print(f"the dealers total is {dealer_total}")
                                                print("the dealer wins")
                                                blackjack()
                                            elif dealer_total < player_total:
                                                print("you win")
                                                wallet += bet_size * 2
                                                print(f"you now have {wallet} in your wallet")
                                                blackjack()
                                        else:
                                            print("invalid input")
                                            hitorstay2()
                                elif player_total > 21:
                                    print(f"{player_total} Player lose, Try again")
                                    print(f"you now have {wallet} in your wallet")
                                elif player_total == 21:
                                    print("Player wins")
                                    wallet += bet_size * 2
                                    print(f"you now have {wallet} in your wallet")
                            player_hit()
                        elif hit_or_stay.capitalize() == "Stay" or hit_or_stay.capitalize() == "S":
                            def player_stay():
                                global player_total, dealer_total, wallet
                                print(f"Player stays with {player_total}")
                                while dealer_total < 17:
                                    dealer_cardaddition = random.randint(1,11)
                                    print(f"the dealer has been dealt {dealer_cardaddition}")
                                    dealer_total += dealer_cardaddition
                                    if dealer_total < 21:
                                        print(f"the dealers total is {dealer_total}")
                                        print(f"Better luck next time")
                                        print(f"you now have {wallet} in your wallet")
                                    elif dealer_total > 21:
                                        print(f"{dealer_total} Dealer lose, Player wins")
                                        wallet += bet_size * 2
                                        print(f"you now have {wallet} in your wallet")
                                    elif dealer_total == 21:
                                        print(f"the dealers total is {dealer_total}")
                                        print("Dealer wins")
                                        print(f"you now have {wallet} in your wallet")
                            player_stay()
                        else:
                            print("invalid input")
                            print()
                            hitorstay()
                elif player_total > 21:
                    print(f"{player_total} Player lose, Try again")
                    print(f"you now have {wallet} in your wallet")
            elif bet_size > wallet:
                print("You don't have enough money")
                print(f"you now have {wallet} in your wallet")
            else:
                print("invalid input, dealing new hand")
                blackjack()
        except ValueError as ve:
            print("invalid input, dealing new hand")
            blackjack()


def maze():
    global result
    while i == 1:
        print("""walking down the corridor you are presented with the option to turn left or right,
        you can hear footsteps but you dont know from which direction""")
        turn = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which way do you turn? (left/right")
        odds = random.randint(1,100)
        if turn == "left":
            print("you have turned left")
            while i == 1:
                if odds <= 30:
                    print("you have walked into the guards, there are too many of them")
                    print("you have been arrested. Game Over")
                    result = "lose"
                    credits()
                    quit()
                    return
                elif odds >=31:
                    print("you have avoided the guards, as the corridor is clear")

                    print("down this corridor you can see a stairway going up and down")
                    stairs = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which way do you go? (up/down")
                    if stairs == "up":
                        print("you have gone up the stairs")
                        odds = random.randint(1,100)
                        while i == 1:
                            if odds <= 30:
                                print("you have walked into the guards, there are too many of them")
                                print("you have been arrested. Game Over")
                                credits()
                                quit()
                            elif odds >=31:
                                print("you have avoided the guards, as the corridor is clear")

                                print("before you there are 2 doors, a red door and a blue door")
                                print("behind one of these doors is the safe room")
                                door = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which door do you choose? (red/blue")
                                odds = random.randint(1,100)
                                if door == "red":
                                    while i == 1:
                                        if odds <= 30:
                                            print("you have walked into the guards, there are too many of them")
                                            print("you have been arrested. Game Over")
                                            credits()
                                            quit()
                                            return
                                        elif odds >=31:
                                            print("you have avoided the guards and you have found the safe room")
                                            result = "win"
                                            return
                                elif door == "blue":
                                    if odds <= 30:
                                        print("you have walked into the guards, there are too many of them")
                                        print("you have been arrested. Game Over")
                                        credits()
                                        quit()
                                        return
                                    elif odds >=31:
                                        print("you have avoided the guards and you have found the safe room")
                                        result = "win"
                                        return
                                
                                else:
                                    print("invalid input, try again")
                    elif stairs == "down":
                        print("you have gone down the stairs")
                        odds = random.randint(1,100)

                        if odds <= 30:
                            print("you have walked into the guards, there are too many of them")
                            print("you have been arrested. Game Over")
                            credits()
                            quit()
                            return
                        elif odds >=31:
                            print("you have avoided the guards, as the corridor is clear")

                            print("before you there are 2 doors, a red door and a blue door")
                            print("behind one of these doors is the safe room")
                            door = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which door do you choose? (red/blue")
                            odds = random.randint(1,100)
                            if door == "red":
                                if odds <= 30:
                                    print("you have walked into the guards, there are too many of them")
                                    print("you have been arrested. Game Over")
                                    credits()
                                    quit()
                                elif odds >=31:
                                    print("you have avoided the guards and you have found the safe room")
                            elif door == "blue":
                                if odds <= 30:
                                    print("you have walked into the guards, there are too many of them")
                                    print("you have been arrested. Game Over")
                                    credits()
                                    quit()
                                    return
                                elif odds >=31:
                                    print("you have avoided the guards and you have found the safe room")
                                    result = "win"
                                    return
                            else:
                                print("invalid input, try again")
                    else:
                        print("invalid input, try again")
        elif turn == "right":
            print("you have turned left")
            while i == 1:
                if odds <= 30:
                    print("you have walked into the guards, there are too many of them")
                    print("you have been arrested. Game Over")
                    result = "win"
                    return
                elif odds >=31:
                    print("you have avoided the guards, as the corridor is clear")

                    print("down this corridor you can see a stairway going up and down")
                    stairs = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which way do you go? (up/down")
                    if stairs == "up":
                        print("you have gone up the stairs")
                        odds = random.randint(1,100)
                        while i == 1:
                            if odds <= 30:
                                print("you have walked into the guards, there are too many of them")
                                print("you have been arrested. Game Over")
                                credits()
                                quit()
                                return
                            elif odds >=31:
                                print("you have avoided the guards, as the corridor is clear")

                                print("before you there are 2 doors, a red door and a blue door")
                                print("behind one of these doors is the safe room")
                                door = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which door do you choose? (red/blue")
                                odds = random.randint(1,100)
                                if door == "red":
                                    while i == 1:
                                        if odds <= 30:
                                            print("you have walked into the guards, there are too many of them")
                                            print("you have been arrested. Game Over")
                                            credits()
                                            quit()
                                            return
                                        elif odds >=31:
                                            print("you have avoided the guards and you have found the safe room")
                                            result = "win"
                                            return
                                elif door == "blue":
                                    if odds <= 30:
                                        print("you have walked into the guards, there are too many of them")
                                        print("you have been arrested. Game Over")
                                        credits()
                                        quit()
                                        return
                                    elif odds >=31:
                                        print("you have avoided the guards and you have found the safe room")
                                        result = "win"
                                        return
                                
                                else:
                                    print("invalid input, try again")
                    elif stairs == "down":
                        print("you have gone down the stairs")
                        odds = random.randint(1,100)

                        if odds <= 30:
                            print("you have walked into the guards, there are too many of them")
                            print("you have been arrested. Game Over")
                            credits()
                            quit()
                            return
                        elif odds >=31:
                            print("you have avoided the guards, as the corridor is clear")

                            print("before you there are 2 doors, a red door and a blue door")
                            print("behind one of these doors is the safe room")
                            door = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which door do you choose? (red/blue")
                            odds = random.randint(1,100)
                            if door == "red":
                                if odds <= 30:
                                    print("you have walked into the guards, there are too many of them")
                                    print("you have been arrested. Game Over")
                                elif odds >=31:
                                    print("you have avoided the guards and you have found the safe room")
                            elif door == "blue":
                                if odds <= 30:
                                    print("you have walked into the guards, there are too many of them")
                                    print("you have been arrested. Game Over")
                                    credits()
                                    quit()
                                    return
                                elif odds >=31:
                                    print("you have avoided the guards and you have found the safe room")
                                    result = "win"
                                    return
                            else:
                                print("invalid input, try again")
          
                    else:
                        print("invalid input, try again")
        else:
            print("invalid input, try again")






def credits():
    print("Thank you for playing 'BROKE FOR LUCK'")
    print("This game was made by:")
    print("Md aktar hossain")
    print("Chris Eaton")
    print("Ben Gardner")
    print("Barbara Adu")
    print("John Sheerin")

def betrayed():
   betray = random.randint(0,100)
   if betray >= 51:
        #win and take money
        print("KILL MARCO")
        ('\n')
        print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + f"\n({name}) You think I'm stupid I know you were behind all this, I said there were only a few people that knew I was coming here but you were the only person from here that knew.")

        print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n Coming up just to the side of you see the other 2 heist partners out of the corner of your eye pull guns and start shooting at you, Quickly you dive behind a concrete post and start to return fire hitting one in the leg and chest. Marco and the other heist partner dive behind the car with loot in and open fire on you. A lucky shot catches you in the arm and you go down dropping your gun under the car.\n 'That's it now' you start thinking to yourself as Marco and the other heist partner make thier way over to finish you off.")
        print("\n")
        print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n Just then you see another car arrive, inside is Maurice and his 2 lackies. 'Just not my day today' you say to yourself as it pulls up beside Marco.")
        print("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(33) + ANSI.style_text(1) + "(Marco)what do you call this you idiots I could have been killed waiting for you to show up, Suddenly you see Maurice and his goons pull out weapons aswel. Knowing it's the end you close your eyes waiting for that final release but then unexpectedly you hear a hail of shots in the direction of Marco and look up to see Maurice taking down Marco.")
        print("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n(Maurice) I never liked that B******d did nothing but treat us like shit, finally deserved his comeupance. Where as you on the other hand you're a very likeable person I can see me and you working well together.")
        print("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + f"\n({name}) Not to be rude or ungreatful but this is not the life I want, I left here to get away from all of this so I would have to decline your offer.")
        print("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n (Maurice)Fair enough I understand your plight I'm not such a bad guy, If your sure I can't convice you to hang around then I'll do you a favor. For all the trouble you've been through and helping me get rid of my little problem I'm gonna let you take one of the loot bags. Enjoy your life and take care.")

        credits() 
        quit()

   elif betray <= 50:
        #get betrayed
        print("TRUST MARCO")
        '\n'
        '\n'
        print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + f"(Marco)({name})How long have we known each other for?, We grew up together, worked together, spent all of our time here together but you left me, You managed to get out of this place whilst I've been stuck here fighting for my life, and you know what that does to you, YOU DON'T DO YOU!, You don't have any idea at all You didn't have to go through it.\n Well fighting through it made me stronger and new opportunities opened up for me and I took them by the throat and strangled the life out of them, every last one of them and took this town for my own.")
        print("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(33) + ANSI.style_text(1) + "\n(Marco)The job you just pulled was in my casino, the other guys with you work for me and as you have probably guessed by now so too does Maurice. I wanted you back here and I knew if I said I needed help you'd come. You left me here to rot and It's my time to repay you for all you've put me through.")

        print_slow("Marco pulls out a gun and shoots you twice in the chest, As you fall to the floor a final gunshot rings out and everything goes black. THE END.")
        credits() 
        quit()


def shootout1():
                global result
                while i == 1:
                    action= input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "looking down the corridor, you can see a guard taking his aim and getting ready to pull the trigger (shoot/hide)")
                    if action.lower() == "shoot":
                        chance = random.randint(1,100)
                        if chance >= 31:
                            print("you aim and successfully shoot the guard")
                            while i == 1:
                                print("the other gaurd was hiding and takes aim")
                                action= input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "what should you do(shoot/hide)? ")
                                if action.lower() == "shoot":
                                    chance = random.randint(1,100) 
                                    if chance >= 31:
                                        print("you aim successfully shoot the gaurd")
                                        while i == 1:
                                            print("the other gaurd was hiding and takes aim")
                                            action= input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "what should you do? (shoot/hide) ")
                                            if action.lower() == "shoot":
                                                chance = random.randint(1,100) 
                                                if chance >= 31:
                                                    print("you aim successfully shoot the gaurd") 
                                                    result = "win"
                                                    return
                                                elif chance <= 30:
                                                    print("you take aim but are shot by the guard, you are killed in action")
                                                    result = "lose"
                                                    return
                                                else:
                                                    print("Error: input unkown")
                                            elif action.lower() == "hide":
                                                print("you took cover protecting yourself from the shooter")       
                                    elif action.lower() <= 30:
                                        print("you take aim but are shot by the guard, you are killed in action")
                                        result = "lose"
                                        return
                                elif action.lower() == "hide":
                                    print("you took cover protecting yourself from the shooter")
                            else:
                                print("Error: input unkown")
                        elif chance <= 30:
                            print("you take aim but are shot by the guard, you are killed in action")
                            result = "lose"
                            return
                    elif action.lower() == "hide":
                        print("you took cover protecting yourself from the shooter")
                    else:
                        print("Error: input unkown")


def shootout2():
                global result
                while i == 1:
                    action= input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "looking down the corridor, you can see a guard taking his aim and getting ready to pull the trigger (shoot/hide)")
                    if action.lower() == "shoot":
                        chance = random.randint(1,100)
                        if chance >= 31:
                            print("you aim and successfully shoot the guard")
                            while i == 1:
                                print("the other gaurd was hiding and takes aim")
                                action= input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "what should you do(shoot/hide)? ")
                                if action.lower() == "shoot":
                                    chance = random.randint(1,100) 
                                    if chance >= 31:
                                        print("you aim successfully shoot the gaurd")
                                        while i == 1:
                                            print("the other gaurd was hiding and takes aim")
                                            action= input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "what should you do? (shoot/hide) ")
                                            if action.lower() == "shoot":
                                                chance = random.randint(1,100) 
                                                if chance >= 31:
                                                    print("you aim successfully shoot the gaurd") 
                                                    result = "win"
                                                    return
                                                elif chance <= 30:
                                                    print("you take aim but are shot by the guard, you are killed in action")
                                                    result = "lose"
                                                    return
                                                else:
                                                    print("Error: input unkown")
                                            elif action.lower() == "hide":
                                                print("you took cover protecting yourself from the shooter")       
                                    elif action.lower() <= 30:
                                        print("you take aim but are shot by the guard, you are killed in action")
                                        result = "lose"
                                        return
                                elif action.lower() == "hide":
                                    print("you took cover protecting yourself from the shooter")
                            else:
                                print("Error: input unkown")
                        elif chance <= 30:
                            print("you take aim but are shot by the guard, you are killed in action")
                            result = "lose"
                            return
                    elif action.lower() == "hide":
                        print("you took cover protecting yourself from the shooter")
                    else:
                        print("Error: input unkown")


def jackpot():
    print("""
    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$
   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$__  $$ /$$__  $$|__  $$__/
      | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$  \ $$| $$  \ $$   | $$   
      | $$| $$$$$$$$| $$      | $$$$$/  | $$$$$$$/| $$  | $$   | $$   
 /$$  | $$| $$__  $$| $$      | $$  $$  | $$____/ | $$  | $$   | $$   
| $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$   | $$   
|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$| $$      |  $$$$$$/   | $$   
 \______/ |__/  |__/ \______/ |__/  \__/|__/       \______/    |__/   
 """)
print("\n")
("\n")
("\n")
print("""
$$$$$$$\                      $$\                       $$$$$$$$\                        $$\                          $$\       
$$  __$$\                     $$ |                      $$  _____|                       $$ |                         $$ |      
$$ |  $$ | $$$$$$\   $$$$$$\  $$ |  $$\  $$$$$$\        $$ |    $$$$$$\   $$$$$$\        $$ |     $$\   $$\  $$$$$$$\ $$ |  $$\ 
$$$$$$$\ |$$  __$$\ $$  __$$\ $$ | $$  |$$  __$$\       $$$$$\ $$  __$$\ $$  __$$\       $$ |     $$ |  $$ |$$  _____|$$ | $$  |
$$  __$$\ $$ |  \__|$$ /  $$ |$$$$$$  / $$$$$$$$ |      $$  __|$$ /  $$ |$$ |  \__|      $$ |     $$ |  $$ |$$ /      $$$$$$  / 
$$ |  $$ |$$ |      $$ |  $$ |$$  _$$<  $$   ____|      $$ |   $$ |  $$ |$$ |            $$ |     $$ |  $$ |$$ |      $$  _$$<  
$$$$$$$  |$$ |      \$$$$$$  |$$ | \$$\ \$$$$$$$\       $$ |   \$$$$$$  |$$ |            $$$$$$$$\\$$$$$$  |\$$$$$$$\ $$ | \$$\ 
\_______/ \__|       \______/ \__|  \__| \_______|      \__|    \______/ \__|            \________|\______/  \_______|\__|  \__|
                                                                                                                                
                                                                                                                                
""")                                                                                                                                

print("A VEGAS HEIST TEXT ADVENTURE")
print("\n")
("\n")
("\n")
input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "PRESS ENTER TO BEGIN")
print("\n")
("\n")
("\n")
("\n")
("\n")
print_slow("Introduction")
print("\n")
("\n")
("\n")
print_slow("\nOctober 28th 9:05pm:")

print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n It was one of those strange days again, beautiful sunny days but less than impressive nights and again this night was no different. The rain was heavy, bouncing off the taxi windows like huge cats and dogs, and the unmistakable smell of damp and glowing neon in the air brought me flashbacks of time spent here previously.\nAll I keep telling myself is I must be crazy coming back to a rat hole like this.")
print("\n")
print_slow("\nI knew though as soon as I got back over the city limits I would be constantly watching my back but at the end of the day I had to come back families more important than anything else.")
print("\n")
print_slow("\nAs the taxi carried on down the I95 and past the airport heading towards the strip I got a phone call from Marco making sure we were still on when I'd had time to settle in. I asked the driver to drop me off at the International villas apartments so I could check-in and grab some food and sleep.")

print("\n")
("\n")
input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  'PRESS ENTER TO CONTINUE')
print("\n")
("\n")
print_slow("October 29th 1:37am:")

print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n I knew things wouldn't be so simple, just got a call from Marco warning me to be careful, There's still a few unsavory chraracters gunning for me so not to get spotted. Think I'm gonna need a some sort of disguise before I go anywhere.")
print(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +"\n")
("\n")

def welcome():
    global name
    name=str(input("enter the name : "))
    if name != "":
        print("\nwelcome to vegas "+ str(name))
        return
    elif name == "":
        print("please enter a name")
        welcome()
welcome()


print("\n")
("\n")
print_slow(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +"October 29th 4:48pm:")
print("\n")
print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n Waliking into the casino I could see many things had changed since I was last in here, they've upgraded the decor entirely, instead of the cluttered machines and tables of old and the run down drab gold and red colours reminiscent of a Roman collesseum and the walked in sticky floors that felt like a lifetime of drinks and cigarette ends had been trampled in it's been swapped out for an ultra modernist and clean setup.")
print("\n")
print_slow( "\n All new machines and tables cover every available inch of the floor, and glass and lights run from floor to ceiling making it too easy to get lost in the place.")

print_slow("\n Walking the casino floor I spot the cashiers desk, think I might aswel have a little flutter while I'm here before I meet up with Marco")
print(ANSI.background(97) + ANSI.color_text(32) + ANSI.style_text(1))
("\n")

# CODE WILL GO HERE FOR 3 CASINO GAMES 
def choosegame():
    game = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "What game would you like to play? (Blackjack,Roulette or Slots)? ")
    if game.capitalize() == "Blackjack":
        blackjack()
        return
    elif game.capitalize() == "Roulette":
        roulette()
        return
    elif game.capitalize() == "Slots":
        slots()
        return
    else:
        print("input invalid, try again")
        choosegame()

choosegame()
print_slow("\nOctober 29th 6:34pm:")
print("\n")

print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n Losing the game shouldn't have been anything unusual but I get the feeling that I've been set up to fail. From one of the side doors three suspicious looking guys started walking over in my direction, two stocky brutes who look like they've been eating steroids for breakfast, lunch and dinner lead by a slim looking businessman with a gotee, Straight away I knew something wasn't right, I was in trouble and I had no way of getting out of here.")
print("\n")
("\n")

print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + f"\n(Maurice)'Nice to finally meet you {name}, My name is Maurice Tarvey, Me and my assciociates have heard a great deal about you, It's nice to have finally met the so called GHOST OF THE STRIP.'")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  f"\n({name})'I guess I should feel blessed then, But what's that got to do with me?.'")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n(Maurice)'Well let me just say we've been led to believe with your unique set of skills that you're the best person to solve our particular problem and you come with such a stellar reputation'.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  f"\n({name})'And here I was thinking I had some fan club follwers dying for an autograph'.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n(Maurice)'Very funny but unfortunately for you not this time. A good friend very kindly passed your name our way and it'll be good business for both of us if you take the time to consider what I'm offering you'.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  f"\n({name})'It dosen't look like I have a chioce really, lead the way mein capitan.'")
print("\n")
("\n")
("\n")
("\n")

print_slow(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +"\nOctober 29th 7:14pm:")
print("\n")
("\n")
("\n")
print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n Leaving the casino floor Maurice and his goon squad led me over to the lounge bar and into the V.I.P area where he proceded to take in one of the booths.")
print("\n")
("\n")
("\n")
print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n(Maurice)'Come take a seat we've got a few things to discuss.'")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  f"\n({name})'So what's so important that you require my services so badly?'")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n(Maurice)'As I said before my boss has taken a vested interesed in you, He's got a little job that needs doing you're going to help us complete it.'")
print(ANSI.background(97) + ANSI.color_text(32) + ANSI.style_text(1) + "\n")
print("\n")
def join():
    player_input = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "So what d'ya say(yes or no): ")

    if player_input.lower() == "no" or player_input.lower() == "n":
        death = random.randint(1,3)
        if death == 1:
            print("PLAYER IS KNOCKED UNCONCIOUS AND WHEN AWOKEN IS BEING DRIVEN OUT INTO THE DESERT, AN GRAVE HAS BEEN DUG OUT AND PLAYER IS SHOT AND THROWN INTO THE GRAVE.")
            credits() 
            quit()
        elif death == 2:
            print("PLAYER IS KNOCKED UNCONCIOUS AND WHEN AWOKEN IS ON TOP OF CASINO ROOF PLAYER IS THEN THROWN OFF THE ROOF.")
            credits() 
            quit()
        elif death == 3:
            print("PLAYER IS KNOCKED UNCONCIOUS AND TAKEN TO A MEAT PACKING FACTORY, PLAYER IS THEN AWOKEN AND TIED UP AND FED INTO MEAT GRINDER.")
            credits() 
            quit()
    elif player_input == "yes" or player_input == "y":
        #player joins heist
        ("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  f"\n({name})'Well I guess I'm all ears so lay it out on the table.'")
        print("\n")
        print_slow("\n(Maurice)'As you may have guessed with your set of skills we don't want you to knock off a candy store, we want you to rob one of our competitors casino's. My boss has many... let's say friends and they're getting a little greedy for thier own good so we want show them a lesson not to mess with us and what better way than taking all thier money.'")
        print("\n")
        print_slow(f"\n({name})'How very original.' 'I'm gonna need to plan and get a team together.'")
        print_slow("\n")
        print(ANSI.background(97) + ANSI.color_text(31) + ANSI.style_text(1) + "\n(Maurice)'Everything has been worked out already and a plan has been put in motion you'll be going in as a team of three, quick and simple. I'll give you all the information you need in due time.'")
        print("\n")
        print("\n(Maurice)'I'll have my guys take you back to your apartment and obviously keep an eye on you, wouldn't want you vanish on us. You can rest up and go over the plans, You've got 2 days then it's go time. Don't let us down or you'll regret it!'")
        print("\n")
        ("\n")
        ("\n")
        print_slow(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +"\nOctober 29th 9:47pm:")
        print("\n")
        ("\n")
        print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n 'Driving back to the apartments I tried to wonder how I got into this situation and who's ratted me out, there's only a few people who knew I was coming back here.") 
        print_slow("\n No time to be racking my head over this moment though need to grab some sleep and get on with going over the plans, 2 days is not nearly enough time to be pulling this thing off.")
        print("\n")
        ("\n")
        ("\n")
        input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "PRESS ENTER TO CONTINUE")
        print("\n")
        ("\n")
        ("\n")
        print_slow("\nOctober 31st 9:36am: Day of the heist")
        print("\n")
        #PICK A ROLE FOR THE HEIST
        def role():
            character_choice = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "Which role do you want to choose: \n A) Distraction. B) Safecracker. C) Mercenary [A/B/C]:")
            if character_choice.capitalize() == "A":
                print_slow("\nYou are the distraction.")
                print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n After going through the details with the other 2 we split up and make our way into the casino. They head over to the lounge to case the area and wait for the signal while I make my way over to the casino floor and put the first part of the plan into action.")
                print("\n")
                print_slow("\nYou are informed of a crooked dealer at the blackjack table 3")
                print_slow("\n I walked over to the Blackjack tables in the far corner of the floor and take a seat at table #3. We got this dealer on our payroll who'll be helping throw the games. It easy to get him onborad when you consider being caught with your pants down with his wifes sister in thier own bedroom, that's not the sort of thing he wants to get out, so he was happy to help.")
                print("\n")
                print_slow("\n(Dealer) Welcome back, trying your luck again")
                print_slow("\n(Dealer) Place your bet")
                print_slow(f"\n({name}) I started with small, $50 in")
                print_slow("\n(Dealer) Feeling lucky today")
                print_slow("\n(Dealer) The dealer draws 9 of hearts and Jack of Spades")
                print_slow("\n(Dealer) Player has 20")
                print_slow("\n(Dealer) Dealer draws 7 of Clubs and Jack of Diamonds")
                print_slow("\n(Dealer) dealer has 18, Well done you've won $100")
                print_slow(f"\n({name}) The dealer gives me a sleight nod, this is where I go big")
                print_slow(f"\n({name}) All in.")
                print_slow("\n(Dealer) You draw King of Diamonds and 6 of Clubs")
                print_slow("\n(Dealer) Dealer draws King of Hearts and Queen of Spades")
                print_slow("\n(Dealer)  Congratulations you've won $300,")
                print_slow(f"\n({name}) Just as I expected I was starting to get crowd now I was winning big, I had people starting to cheer me on.")
                print_slow(f"\n({name}) I put another bet in $300, Let's make it interesting double up again.")
                print_slow(f"\n({name}) Shocks from the crowd and the table.")
                print_slow("\n(Dealer) You draw 6 of Hearts and 8 of Clubs, Player has 14")
                print_slow(f"\n({name}) I decidded to hit again, and draw 7 of Hearts.")
                print_slow("\n(Dealer) Player has 21")
                print_slow("\n(Dealer) Well done again sir you've won $600.")
                print_slow(f"\n({name}) The tables more shocked now and a bigger crowd is gathering around me.")
                print_slow(f"\n({name}) I look to the dealer and he gives me another nod, this is the moment now and I move into the next phase of the plan")
                print_slow(f"\n({name}) The crowd are all stood around the table now as I shout 'ALL IN AGAIN' and the crowd go mental.")
                print_slow("I place the bet of $600.")
                print_slow("\n(Dealer) 10 of diamonds and the Queen of Spades, player has 22, player bust")
                print_slow(f"\n({name}) I could hear the crowd gasp with the draw, So I start on the dealer shouting and pushing at him.")
                print_slow(f"\n({name}) the dealer gets in on it too and pushes me back, knocking me off my chair")
                print_slow(f"\n({name}) I get up and jump at the dealer, necxt thing I know the alarms start ringing and security comdes charging over.")
                print_slow(f'\n({name}) Ok now the real show starts')
                



            
                def fight1() :
                    fightA = (input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  '6 wild bouncers appear fight them or runt towards slots F/R? '))
                    if fightA.capitalize() == 'F':
                        print ('The bouncers overpower you and take out off the casino floor')
                        credits()
                        quit()
                    elif fightA.capitalize()=='R':
                        print ('one bouncer trips over handbag and twists his ankle')
                    else:
                        print ('Invalid Input')
                        fight1()
                fight1()
                
                def fight2() :                    
                    fightB = (input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  '5 Wild bouncers surround you at the slots, stand and Fight or throw the old ladies cup of coins at bouncer 3 F/R?'))
                    if fightB.capitalize() == 'F':
                        print ('The bouncers overpower you and take out off the casino floor')
                        credits()
                        quit()
                        
                    elif fightB.capitalize()=='R':
                        print ('you hit bouncer 3 and 4 directly in the eyes push both of them over creating an escape path towards the bar')
                        
                    else:
                        print ('Invalid Input')
                        fight2()
                fight2()
                
                def fight3() :
                    fightC = (input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  '3 wild bouncers appear stand and fight or run towards the stage show F/R? '))
                    if fightC.capitalize() == 'F':
                        print ('The bouncers overpower you and take out off the casino floor')
                        credits()
                        quit()
                        x=1
                    elif fightC.capitalize()=='R':
                        print ('a random hero puts out a leg and trips the bouncer onto a table with a few unsavoiry looking men')
                        x=1
                    else:
                        print ('Invalid Input')
                        fight3()
                fight3()    
                
                def fight4() :
                    fightD = (input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  '2 wild bouncers appear Its time to fight... Attack bouncer 1 or bouncer 2? 1/2?'))
                    if fightD.capitalize() == '1':
                        print ('The bouncers overpower you and take out off the casino floor')
                        credits()
                        quit()
                        
                    elif fightD.capitalize()=='2':
                        print ('Roundhouse kick connects perfectly you and bouncer 1 are in shock')
                        print ('You pick up the nearest object... Its a bottle of your favorite liqor')
                        
                    else:
                        print ('Invalid Input')
                        fight4()
                fight4()
                
                def OneVsOne() :
                    OneVOne = (input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  'drink whole bottle or break it on bouncer 1s face Drink/Break? '))
                    if OneVOne.capitalize() == 'Drink':
                        print ('Bouncer 1 overpowers you and take out off the casino floor')
                        credits()
                        quit()
                    elif OneVOne.capitalize()=='Break':
                        print ('you have defeated all the bouncers distraction successful, time to meet the others at the rendevous')
                    else:
                        print ('Invalid Input')
                        OneVsOne()
                OneVsOne()
                '\n'
                '\n'
                '\n'
                '\n'
                print (ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + " Theres an eerie sense felling about this, where was hell was Maurice and those thugs during all of this?")
                print (" I need to get a drink, a stiff one...")
                print (" I'm done in this town I need to get out of Vegas tonight")
                print (" If I've been done over like this Can I even trust the other guys?")
                print (" Can I even trust Marco, he sent me to this hell hole knowing about Maurice, Just wait till I see that little rat.")
                print (" How long till the cops arrive?, My mugshots will be all over now I've got nowhere to hide")
                print (" My mind is racing... why did I agree to this what should I do?")
                
                def choicea():
                    choice_one = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  'Forget the money and leave now Yes/No? ')
                    if choice_one.capitalize() == ('Yes'):
                        print('You run towards the exit, as you approach the doors your surrounded by police with their guns drawn')
                        credits() 
                        quit()
                    if choice_one.capitalize() ==('No'):
                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  ' Theres one more thing I need to do, lets see this thing through till the end')
                        print('Heads towards the Underground Carpark')
                    else:
                        print('Invalid Input')
                        choicea()
                choicea()

            elif character_choice.capitalize() == "B":
                print("You are the safecracker.")

                print("\n")
                ("\n")

            # this is safecracker role
                print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n Meeting up in the lounge with the mercenary we go over our plan, making sure we've got everything down to a tee. We can't have anything go wrong at this point or it's game over.")
                (ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "\nWe make sure we've got all the guards routes checked down to the millisecond, What staff are working on what duty and changeover times. As expected all guards are armed so we'll have to be quick and on point not to get our arses handed to us on a plate.")
                print("\n")
                print_slow("\n Then it's just relying on the distraction to carry out thier job and that should give us ample opportunity to get in and get the job done before anyone notices whats gone on.")
                print("\n")
                ("\n")
                print("\nOctober 31st 7:18pm:")
                print("\n")
                ("\n")

                print_slow("\nHeading into the casino we split up, me and the mercenary head towards the side door readying ourselves to proceede into the back area and the the distraction heads over towards the casino floor to buy us the time needed to get in and get the job done. Hearing some loud shouts and cheers we could just about see from where we were that things were starting to go to plan as the distraction was gaining quite a bit of attention over at the gambling tables.")
                print_slow("\nRight on queue the distraction moved into the next phase of the plan and let's just say they've gone above and beyond what's expected as the shit's just hit the fan.")

            # choose to force entry to secure area or steal keycard

                player_input = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "what would you like to do? steal or force? ")
                print("\n")
                ("\n")

                if player_input == "steal" or player_input.lower == "steal":
                    print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "\nAs a guard came rushing out of the side door I made my move and accidentally ran into him whilst quickly swiping his keycard off his belt. With that done we made our way through the side door and navigated through the maze of corridors towards the elevator/stairs and down to the vault.")
                elif player_input == "force" or player_input.lower == "force":
                    print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "\nWe forced our way in to the secure area as 2 guards came rushing out to help deal with the problem the distraction had caused, We subdued them and then made our way further into the back heading towards the elevator/stairs and down to the vault. Before we had chance to go down we were drawn into a shootout with a couple of have ago heroes, It didn't take long to take them out with the crackshot merc with me and a couple of precise hits later and the guards were out. I'll give Maurice some credit he's spared no expense on the hired help at least I've got people who can actually do thier job properly.")
                print("\n")
                ("\n")
                print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "At the end of the corridor we had the option of taking the elevator or stairs down to the vault.")
                print("\n")
                ("\n")

            # choose to take elevator/stairs down to the vault
                def elevator_stairs():
                    player_input = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  ("Take the elevator/stairs? "))
                    if player_input == "elevator" or  player_input.lower == "elevator":
                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "Taking the quick way down in the elevator we ran into another set of guards waiting just outside the elevator in the corridor leading to the vault which resulted in another intense shootout, But again they were no match were dispatched easliy enough. We dragged the bodies into one of the side rooms out of sight.")
                    elif player_input == "stairs" or player_input.lower:
                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "Even though it was a slower route down to the vault it gave us the jump on a couple of guards that were patroling the corridor down to the vault. Quickly and quietly we took them out and hid the bodies in one of the filling rooms.")
                    else:
                        print("Invalid Input")
                        print("Choose one of the options to proceede")
                        elevator_stairs()
                    print("\n")
                    
                elevator_stairs()
                ("\n")
                print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  "\nWe reached the vault room at the far end of the corridor, and looking at the make and model of the safe it was time to begin. lets crack the safe.")
                print("\n")
                ("\n")
                
                

                def cracksafe():
                    global attempts1
                    while attempts1 <= 3:
                            number1 = random.randint(0,100)
                            number2 = random.randint(0,100)
                            number3 = random.randint(0,100)
                            number4 = random.randint(0,100)
                            number5 = random.randint(0,100)

                            print(f"{number1},{number2},{number3},{number4},{number5}")
                            numbers = [number1,number2,number3,number4,number5]
                            numbers.sort(reverse=True)
                            try:
                                input1 = int(input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "which is the largest number? "))
                                if input1 == numbers[0]:
                                    print("winners")

                                    input2 = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  ("what planet has the most moons? "))
                                    planet = "Saturn"
                                    if input2 == planet or input2.capitalize() == planet:
                                            print("Correct, time for the last question") 

                                            input3 = input (("what is the world fastest bird?"))
                                            bird = "Falcon"
                                            if   input3 == bird or input3.capitalize() == bird:
                                                print("Winner")
                                                jackpot()
                                                break
                                            else:#third question wrong
                                                print("wrong answer")
                                                attempts1 += 1
                                    else:#second question wrong
                                        print("wrong answer")   
                                        attempts1 += 1
                                else:#first question wrong
                                    print("wrong answer")
                                    attempts1 += 1
                            except ValueError:
                                print("Invalid Input")
                                cracksafe()

                cracksafe()
                    

                if attempts1 >= 4:
                    print(
                    ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """The safecracker fails to open the safe and is unable to get it to open, 
                    at this moment the mercenary and the safe cracker know its over,
                    they are not going to escape and decide to surrender themselves. (GAME OVER)
                    """)
                    credits()
                    quit()
                else:
                    # OPTION A WILL CONTINUE WITH THE STORY OPTION B WILL TRIGGER THE PASSCODE MINIGAME
                    print("\n")
                    ("\n")
                    ("\n")
                    print_slow( "\n With safe now open we take a look inside, And Maurice wasn't joking when he said his friends were getting a little greedy, there must be close to a hundred million in here. Well it's coming with us now.")
                    print_slow("\n It took us a few minutes to pack up the bags with the loot, with that done it was time to make a sharp exit before they cotton on to what's happened and we have an army on our backs.")
                    print_slow("\n We made our way back up to the ground floor and into the laundry room where we had change of clothes stashed ready for our escape.")
                    print_slow("\n We left the casino out through the laundry entrance and bundled the loot and gear into our waiting laundry van and exited out of the service gate heading for the rendevouz location in an underground carpark at the airport.")
                    print("\n")
                    ("\n")

            elif character_choice.capitalize() == "C":
                def merc_stealorforce():
                    action = input(ANSI.background(97) + ANSI.color_text(37) + ANSI.style_text(1) +  "you have 2 choice forced entry or Stealing a key card, which do you choose? Steal or Force?")
                    if action.capitalize() == "Force":
                        #mercenary forced entry
                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """the mercenary walks in the bar. 
                        the bar was quite nice place to have a drink with other customers. 
                        the mercenary ordered a drink and he was looking around the bar. 
                        he meets the safe cracker in the bar. 
                        the marcenery was looking for the cameres and the security guards. 
                        he notices a door with that is heavily guarded with 3 security cameras covering the door. 
                        the mercenary and the safecracker take there drinks and head over to the empty seats near the door.
                        he was waiting for the place to become quiet so that he can make the safe move with the safe cracker.

                        """)

                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """hear distruction, in the meanwhile, mercenary heard the noise from the bar.
                        there was a fighting going on with two customers and the security. 
                        most of the securities were dealingwith the situation. 
                        mercenary was looking around to make the move
                        """)

                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """mercenary was watching the fighting. one cutomer call police and shouting to the security. 
                        all othercustomers were in panic. the enviroment of the casino was totally changed. 
                        few of the customers were already left the casino. 
                        mercenary was waiting for the securities to go awayfor the place where he was sitting so that he can make a move to the safe. 
                        onlytwo securities remain on the premises.
                        """)

                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """When mercenary saw that only two bouncers were remaining on the floor, 
                        he went closer to them and attacked on them. 
                        He knocked them unconscious. Now there were no one to stop the mercenary and he was free to go. 
                        He steels the key card from one of the bouncer so that he can enter the door which was guarded.

                        """)

                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """Mercenary gets the key from one of the bouncers and he enter the corridor. 
                        As soon as he enters the corridor, he hears the sound of shootout.  
                        The security guards who are on the duty for that corridor they started to shoot the mercenary. 
                        No one was there but only the mercenary.

                        """)

                        
                        shootout1()
                        if result == "lose":
                            print("""Option lose mercenary starts to shoot to the guards. 
                            He was trying to knock the guards down. From the other side guards were shooting at him. 
                            After a few minutes of fighting, mercenary was out of bullets. Then guards killed the mercenary.

                            """)


                        elif result == "win":
                            print("""Option win: mercenary starts to shoot the bad guys. He was trying to kill the bad guys. 
                            Bad guys were shooting at him but the mercenary was able to kill the bad guys. 
                            Mercenary finds the safe room and they enter. 

                            """)
                        
                        shootout2()

                        if result == "lose":
                            print("""
                            in the safe room alarm goes on and securities alerts that they are in safe room. mercenary starts to shoot to the guards. He was trying to knock the guards down. From the other side guards were shooting at him. After a few minutes of fighting, mercenary was out of bullets. Then guards killed the mercenary.
                            """)

                        elif result == "win":
                            print("""
                            mercenary starts to shoot the bad guys. He was trying to kill the bad guys. Bad guys were shooting at him, but the mercenary was able to kill the bad guys. Safe cracker opens the safe and the begin to steal. They try to steal as much as they can as they do not have much time. Time is running out as the back up on the way.

                            """)


                            print("""The mercenary and the safe cracker were stealing. They took as much as money as they can. In the meantime, they hear a searing sound. They realised that somebody is coming to catch them. So, they took the money and rush to escape from the safe room. 

                            """)
                            betrayed()


                    elif action.capitalize() == "Steal":
                        
                        print(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """In the bar, 
                        the mercenary is notified of a heavily armed door he looks around and can see many people entering the area dressed in suits with badges and ear pieces. 
                        They look like security guards, they enter the guarded door in walking in a strange formation. 
                        They enter behind the door. The mercenary continues looking around for a quiet way in. he orders a drink with the safe cracker and they move closer to the door. 
                        Trying to gather more information. Waiting in the bar he see the doors swing open with the guards he saw before circling one man in the middle, 
                        this man looks to be of great importance, in his chest pocket there is a badge. 
                        This is the key to getting behind the door.
                        """)


                        print(
                        ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """The mercenary is looking for a way to steal the key card, 
                        a noise is heard coming from the casino floor a fight has broken out with a customer, 
                        looking over the mercenary can se that this is there accomplice giving them a chance to act. 
                        As the fight breaks out security surround the man with the key card forcing him to take cover as he does the key card falls to the floor, 
                        noticing this the mercenary act quickly to steal the card allowing them to get through the door.
                        """)



                        print(
                        ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """After entering the corridor the mercenary and safecracker can see an alarm ringing, 
                        they know they must be quiet or else security will catch them. They need to find the room with the safe.
                        Walking down the corridor they can hear that the alarm has stopped. 
                        They now know time is of the essence and must find the safe room. 
                        They can hear footstep in the corridor but don’t know which way. 
                        The mercenary must now guess which way they need to go to travel safely.

                        """)

                        maze()

                        
                        print(
                        
                        ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """The safe cracker approaches the safe and begins to get to work opening the safe. 
                        Keeping an eye on the corridor, suddenly an alarm  begins to ring out, 
                        the mercenary and the safe cracker have been spotted in the safe room, 
                        the alarm ringing out around the casino alerts security sending them to the safe room. 
                        The mercenary is now forced into a shoot out with security.

                        """)
                        
                        shootout2()
                        if result == "lose":
                            print(
                            ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """The mercenary looses the shootout and takes a bullet to the shoulder, 
                            unable to raise his weapon the mercenary takes a second bullet to the chest, 
                            falling down the mercenary is surrounded by security, 
                            the mercenary vision slowly fades to black as he looses consciousness. (GAME OVER)
                            """)
                            credits()
                            quit()


                        elif result == "win":
                            print(
                            ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """The mercenary is able to take out the security that was shooting at them as the safecracker opens the safe, 
                            they procced quickly to fill their bags with as much money as they can as time is running out as back up is on its way.
                            """)

                            print(
                            ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  """They take the bags and being making there way to the planned exit point out the back of the casino,
                            as they begin approaching the exit they can hear music playing that suddenly comes to a crashing halt, 
                            gun shots are heard and screaming from a crowd echoes down the corridor, 
                            suddenly a stage door crashes open, 
                            the mercenary raises his gun ready to fire when there accomplice who caused the distraction comes rushing though the door, 
                            relived to see each other. The accomplice take some of the bag and they begin making there way to the exit, 
                            they can see the getaway car waiting for them.
                            """)
                    else:
                        print("Invalid input")
                        merc_stealorforce()
                merc_stealorforce()
            else:
                print ("Invalid input")
                role()
        role()     
    else:
        print("input invalid, try again")
        join()
join()

print('mercenary and the distraction reached the get away point of the game')
'\n'
   
print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n After leaving the service entrance of the casino the Mercenary and Safecracker head over to the warehouse on Crestline Loop to dump the laundry van and change vehicles then over to the redevouz point at the airport where they are to meet up with the Distraction.")

print_slow( ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + "\n The Distraction having left the casino a while earlier had a few stops to make on the way to the redevouz as they had to be sure they weren't being tailed. Once they were sure they were in the clear they headed over the airport to meet-up with the other 2.")

print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) +  f"In the airport carpark the 3 meet up and are sat in a dark blue Ford waiting for Maurice to show up when stepping out from behind a black van Marco starts walking over, Suprised to him here ({name}) tells the other 2 to wait there with the loot while they get out of the car and make thier way over to him. With everything that's gone down over the past few days he's got alot of questions they want answers to.")

print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + f"\n({name}) What the hell are you doing here?")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(33) + ANSI.style_text(1) + "\n(Marco)I need to speak with you quickly.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + f"\n({name}) What do you mean, I've been trying to call you for the past 2 days, Is it you that set me up there was only a few people that knew I was coming back here and as soon as I get here I'm suddenly drawn into this. You've got some answering to do before I lose my shit and pop you here.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(33) + ANSI.style_text(1) + "\n(Marco)It wasn't me I had nothing to do with anything, I wouldn't do that to you, You have to believe me.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(34) + ANSI.style_text(1) + f"\n({name}) It's just a little too convenient you showing up here at this time, Did you rat me out? are you in on this with Maurice.")
print("\n")
print_slow(ANSI.background(97) + ANSI.color_text(33) + ANSI.style_text(1) + "\n(Marco)No, no I'm not, You're crazy I'm telling you the truth.")

betrayed()
credits()
quit() 


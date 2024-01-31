import random
import sys

name = input("Enter your first name: ")
print("\n")
waiver_signed = input(
    "Your signature(first name) if you want to participate in the game , knowing that you can die : ")
print("\n")

if name.lower() == waiver_signed.lower():
    print("Game has begun \n")

    def game():
        while True:
            empty_shells = random.randint(1, 7)
            bullets = random.randint(1, 7)
            if empty_shells + bullets == 8:
                str_empty = str(empty_shells)
                str_bullets = str(bullets)
                new_empty = (empty_shells-1)
                str_new_empty = str(new_empty)

                print("Empty Shell(s): " + str_empty +
                      " Bullet(s): "+str_bullets+"\n")
                while True:
                    live_round = random.choice([empty_shells, bullets])
                    trigger = input(
                        "To shoot yourself,use key 's' or to shoot the dealer use key 'd' ")

                    # Game over in first shot
                    if trigger == "s" and live_round == bullets:
                        print("Game over! you shot yourself")
                        sys.exit()
                        break

                    elif trigger == "d" and live_round == bullets:
                        print("Game over! you shoot the dealer")
                        sys.exit()
                        break

                    # Game continues with dealer having a choice
                    elif trigger == "s" and live_round == empty_shells:

                        print("You survived now empty shells left : " +
                              str_new_empty + " Bullets : " + str_bullets)
                        if new_empty == 0:
                            print("No more empty shells left , game over")
                            sys.exit()
                            break

                        else:
                            print("\n Dealer's turn \n")
                            dealer_choice = random.choice("s" "p")
                            dealer_live_round = random.choice(
                                [new_empty, bullets])
                            dealer_new_empty = new_empty-1
                            str_dealer_new_empty = str(dealer_new_empty)
                            if dealer_choice == "s" and dealer_live_round == bullets:
                                print("You won! , The Dealer shot himself")
                                sys.exit()
                                break
                            elif dealer_choice == "p" and dealer_live_round == bullets:
                                print("You lost, The Dealer shot you ")
                                sys.exit()
                                break
                            elif dealer_choice == "s" and dealer_live_round == new_empty:
                                print("The Dealer survived and now empty shells left : " +
                                      str_dealer_new_empty + " Bullets : " + str_bullets)
                                continue
                            elif dealer_choice == "p" and dealer_live_round == new_empty:

                                print("You survived and now empty shells left : " +
                                      str_dealer_new_empty + " Bullets : " + str_bullets)
                                continue
                    elif trigger == "d" and live_round == empty_shells:

                        print("The dealer survived now empty shells left : " +
                              str_new_empty + " Bullets : " + str_bullets)
                        if new_empty == 0:
                            print("No more empty shells left , game over")
                            sys.exit()
                            break

                        else:
                            print("\n Dealer's turn \n")
                            dealer_choice = random.choice("s" "p")
                            dealer_live_round = random.choice(
                                [new_empty, bullets])
                            dealer_new_empty = new_empty-1
                            str_dealer_new_empty = str(dealer_new_empty)
                            if dealer_choice == "s" and dealer_live_round == bullets:
                                print("You won! , The Dealer shot himself")
                                sys.exit()
                                break
                            elif dealer_choice == "p" and dealer_live_round == bullets:
                                print("You lost, The Dealer shot you ")
                                sys.exit()
                                break
                            elif dealer_choice == "s" and dealer_live_round == new_empty:
                                new_empty = new_empty-1
                                print("The Dealer survived and now empty shells left : " +
                                      str_dealer_new_empty + " Bullets : " + str_bullets)
                                continue
                            elif dealer_choice == "p" and dealer_live_round == new_empty:
                                print("You survived and now empty shells left : " +
                                      str_dealer_new_empty + " Bullets : " + str_bullets)
                                continue

            else:
                continue
    game()
else:
    print("Your sign doesn't match your name")
    sys.exit()

import random
import sys
name = input("Enter your first name: ")
print("\n")
waiver_signed = input(
    "Your signature(first name) if you want to participate in the game , knowing that you can die : ")
print("\n")

if name.lower() == waiver_signed.lower():
    print("Game has begun\n")

    def game():
        while True:
            empty = random.randint(0, 7)
            bullets = random.randint(0, 7)
            if empty + bullets == 8:
                Empty = str(empty)
                Bullets = str(bullets)
                New_Empty = str(empty-1)
                print("Empty Shell(s): " + Empty + " Bullet(s): "+Bullets+"\n")

                while True:
                    live_round = random.choice([empty, bullets])
                    trigger = input(
                        "To shoot yourself, use key 's' or to shoot the dealer use 'd' ")

                    if trigger == "s" and live_round == bullets:
                        print("Game over you died")
                        break
                        sys.exit()
                    elif trigger == "s" and live_round == empty:
                        print("You can continue and now empty shells : " +
                              New_Empty + " Bullets : " + Bullets)
                        if New_Empty == 0:
                            print("No more empty shells and game over")
                            break
                            sys.exit()
                        else:
                            New_Empty = str(int(New_Empty)-1)
                            continue

                    elif trigger == "d" and live_round == bullets:
                        print("You won the game and you killed the dealer")
                        break
                        sys.exit()
                    elif trigger == "d" and live_round == empty:
                        print("The Dealer survived now empty shells : " +
                              New_Empty + " Bullets : " + Bullets)
                        if New_Empty == 0:
                            print("No more empty shells and game over")
                            break
                            sys.exit()
                        else:
                            New_Empty = str(int(New_Empty)-1)
                            continue
                break  # Exit the loop if the condition is met
            else:
                continue  # Rerun the loop to generate new random numbers
    game()
else:
    print("Game has ended because signature doesn't match name.")

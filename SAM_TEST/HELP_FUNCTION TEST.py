def helper(context):
    user_input = input("Enter your choice: ")
    if user_input.casefold == "/help":
        if context == "rr_game":
            print("You're on your own now. You signed up for this.")
            user_input_2 = input("Select your choice: ")
            return user_input_2
        elif context == "trainer_battle":
            print("In a Pokemon Battle, you command your Pokemon by writing their attacks correctly.")
            print("Remember that attack commands are case sensitive. So pay attention to capital letters.")
            print("Once you defeated the opponent, you can choose to add that Pokemon to your Team.")
            print("Remember, you are a criminal on the run, and will not be able to have more than 6 Pokemon.")
            print("That means, you wont store excess Pokemon in a PC, your only option is to release them.")
            user_input_2 = input("Select your choice: ")
            return user_input_2
        elif context == "Poker":
            print("Play Poker, bet your Pokemon on the line. Remember.")
            user_input_2 = input("Select your choice: ")
            return user_input_2
        else:
            user_input_2 = input("Select your choice: ")
            return user_input_2
    else:
        return user_input

x = helper("trainer_battle")
print(x)
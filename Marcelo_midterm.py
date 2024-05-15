import os
# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    # Add more games as needed
}

# Dictionary to store user accounts with their balances and points
user_accounts = {}

# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# Function to rent games
def rent_games(username):
    game_key = list(game_library.keys())
    total = float(0)
    display_available_games()
    print("=========================")
    print(f"Balance: ${user_accounts[username]['balance']}")
    while True:
        try:
            shopping = int(input("what item would you like to buy(leave blank to return): "))
        except Exception:
            print("Please try a valid Input..")
            continue
        if shopping == "":
            return logged_in_menu(username)
        shopping -= 1
        shopping = game_key[shopping]
        user_accounts[username]['inventory'].append(shopping)
        print("Current Game in cart:")
        print(f"{user_accounts[username]['inventory']}")
        total = game_library[shopping]['cost'] + total
        game_library[shopping]['quantity'] -= 1
        while True:
            try:
                confirm = input("would you like to add more?(Y/N):").lower()
            except Exception:
                print("Please only input 'Y' for YES and 'N' for NO.")
                continue
            
            if confirm == "y":
                break
            elif confirm == 'n':
                gain_points = total / 2
                user_accounts[username]['points'] = gain_points
                print(f'gained Points: {user_accounts[username]['points']}')
                total = float(user_accounts[username]['balance'] - total)
                if total <= 0:
                    print('Insufficient Balance..')
                    logged_in_menu(username)
                    user_accounts[username]['inventory'].clear()
                else:
                    user_accounts[username]['balance'] = total
                    print("Games Successfully rented..")
                    print(f"New Balance: {user_accounts[username]['balance']}")
                    print('Press ENTER to return')
                    input()
                    os.system('cls')
                    return logged_in_menu(username)
            else:
                print("Please only input 'Y' for YES and 'N' for NO.")
            
# Function to register a new user
def register_user():
    while True:
        username = input("Enter username(leave blank to return):")
        if username =="":
            return
        if username in user_accounts.keys():
            print("Username already taken. Try again")
        else:
            break
    
    while True:
        password = input("Enter password(must be more than 5 characters): ")
        if len(password) >= 5:
            user_accounts.update({username: {'password': password, 'balance':0.00, 'points': 0,  'inventory': []}})
            print("=========================")
            print("---Account registered---")
            print("=========================")
            print("Press Enter to continue and Log in.. ")
            input()
            return
        else:
            print("Password must be 5 or more characters")

# Function to display available games with their numbers and rental costs
def display_available_games():
    i =1
    print("Available Games:")
    print(f"{'Game Name':<25} {'Price':<8} {"Copies":<10}")
    for items in game_library:
        if game_library[items]['quantity'] != 0:
            print(f"[{i}]{items:<20}: {"":<2}${game_library[items]['cost']:<3} :{"":<4}{game_library[items]['quantity']:<10}")
            i += 1

# Function to return a game
def return_game(username):
    display_inventory(username)
    print("=========================")
    while True:
        print("Please refer to the games number Above\n(Leave blank to go back)")
        try:
            
            returning_item = int(input("Which Game would you like to return: "))
        except Exception:
            print("Please try a valid Input..")
            continue
        if returning_item == "":
            return
        returning_item -= 1
        returning_item = user_accounts[username]['inventory'][returning_item]
        user_accounts[username]['inventory'].remove(returning_item)
        while True:
            try:
                confirm = input(f"Are you sure you want to return [{returning_item}]?(Y/N):").lower()
            except Exception:
                print("Please only input 'Y' for YES and 'N' for NO.")
                continue
            if confirm == 'y':
                game_library[returning_item]['quantity'] += 1
                print("Game Successfully Returned..")
                print("Press Enter to continue")
                input()
                os.system('cls')
                logged_in_menu(username)
            elif confirm == 'n':
                print("Returning to main menu..")
                return
            else:
                print("Please only input 'Y' for YES and 'N' for NO.")

# Function to top-up user account
def top_up_account(username):
    print("Before you can Rent a game, you must top-up your account first..")
    while True:
        try:  
            amount = float(input("Amount(leave blank to return): "))
        except Exception:
            print('Incorrect Input. Please try Again.')
            continue
        if amount == "":
            return
        if amount <= 0:
            print('Please input a proper amount..')
        else:
            try:
                confirm = input('Pleas confirm that it is the right amount(Y/N): ').lower()
            except Exception:
                print("Please only input 'Y' for YES and 'N' for NO.")   
                continue
            if confirm == 'y':
                user_accounts[username]['balance'] = amount
                print('Balance Successfully updated..')
                return
            elif confirm == 'n':
                print('Returning to main menu..')
                return
            else:
                print("Please only input 'Y' for YES and 'N' for NO.")
                
# Function to display user's inventory
def display_inventory(username):
    i=1
    print("Rented Games:")
    print(f"{'Game Name'}")
    for items in user_accounts[username]['inventory']:
        print(f"[{i}]{items:<20}")
        i+=1

# Function for admin to update game details
def admin_update_game():
    game_key = list(game_library.keys())
    display_available_games
    while True:
        print("Refer to the Game's number Above\n(Leave blank to return)")
        try:
            edit_choice = int(input("Enter the Game you need to edit: "))
        except Exception:
            print('Incorrect Input. Please try Again.')
            continue
        if edit_choice == "":
            return
        edit_choice -=1
        edit_choice = game_key[edit_choice]
        print("=========================")
        while True:
            try:
                new_price = float(input("Enter new Price: "))
                new_copy = int(input("Enter new Quantity: "))
            except Exception:
                print("Please input a numerical value..")
                continue
            if new_price <= 0 or new_copy <= 0:
                print('Please Input a valid Value..')
            while True:
                try:
                    confirm = input("Please confirm the correct information?(Y/N):").lower()
                except Exception:
                    print("Please only input 'Y' for YES and 'N' for NO.")
                    continue
                if confirm == 'y':
                    game_library[edit_choice]['cost'] = new_price
                    game_library[edit_choice]['quantity'] = new_copy
                    print("Game Successfully Updated..")
                    print("Press ENTER to return to the main menu..")
                    input()
                    os.system('cls')
                    return
                elif confirm == 'n':
                    print("Press ENTER to return to the main menu..")
                    input()
                    os.system('cls')
                    return

# Admin menu
def admin_menu():
    print('============================')
    print(f"Welcome Admin")

    while True:
        print("{1} Browse Game\n{2} Update Game\n{3} Log out")
        try:
            main_choice = int(input("Enter Choice: "))
        except Exception:
            print("Please enter 1-3 only")
        if main_choice == 1:
            display_available_games()
        elif main_choice == 2:
            admin_update_game()
        elif main_choice == 3:
            print("=============================")
            print("---Thank you and good bye---")
            print("=============================")
            exit()
        else:
            print("Please enter 1-3 only")

# Function for users to confirm redeem points for a free game rental
def redeem_free_rental(username):
    os.system('cls')
    print("=====================CONGRATULATION=====================\n")
    print("!!-You have enough points to redeem a FREE Game Rental-!!\n")
    print("=====================CONGRATULATION=====================")

    while True:
        try:
            confirm = input("Would you like to redeem it?(Y/N): ")
        except Exception:
            print("Please only input 'Y' for YES and 'N' for NO.")
            continue
        if confirm == 'y':
            free_rental(username)
        elif confirm == 'n':
            print("Press ENTER to return to the main menu..")
            input()
            os.system('cls')
            return
        else:
            print("Please only input 'Y' for YES and 'N' for NO.")

#Function to Redeem the free game rental
def free_rental(username):
    user_accounts[username]['points'] -= 3
    game_key = list(game_library.keys())
    i =1
    print("Available Games:")
    print(f"{'Game Name':<25} {"Copies":<10}")
    for items in game_library:
        if game_library[items]['quantity'] != 0:
            print(f"[{i}]{items:<20}:{"":<4}{game_library[items]['quantity']:<10}")
            i += 1
    print("=========================")
    while True:
        try:
            redeem = int(input("what Game would you like to Redeem(leave blank to return): "))
        except Exception:
            print("Please try a valid Input..")
            continue
        if redeem == "":
            return logged_in_menu(username)
        redeem -= 1
        redeem = game_key[redeem]
        user_accounts[username]['inventory'].append(redeem)
        print("Current Game in cart:")
        print(f"{redeem}")
        
        while True:
            try:
                confirm = input("Are you sure you want to redeem this Game?(Y/N):").lower()
            except Exception:
                print("Please only input 'Y' for YES and 'N' for NO.")
                continue
            
            if confirm == "y":
                game_library[redeem]['quantity'] -= 1
                print("Game successfully Redeemed...")
                print('Thank you for Shopping with us!!')
                print("Press ENTER to return to the main menu..")
                input()
                os.system('cls')
                return logged_in_menu(username)
                
            elif confirm == 'n':
                break
            else:
                print("Please only input 'Y' for YES and 'N' for NO.")

# Function to handle user's logged-in menu
def logged_in_menu(username):
    print('============================')
    print(f"Welcome {username}")
    if user_accounts[username]['points'] >= 3:
        redeem_free_rental(username)
    if user_accounts[username]['inventory'] != None:
        print(f"Rented: {user_accounts[username]['inventory']}")
    while True:
        print("{1} Rent\n{2} Return\n{3} Log out")
        try:
            main_choice = int(input("Enter Choice: "))
        except Exception:
            print("Please enter 1-3 only")
        if main_choice == 1:
            if user_accounts[username]['balance'] == 0:
                top_up_account(username)
            else:
                rent_games(username)
        elif main_choice == 2:
            return_game(username)
        elif main_choice == 3:
            print("=============================")
            print("---Thank you and good bye---")
            print("=============================")
            exit()
        else:
            print("Please enter 1-3 only")
                
# Function to check user credentials
def check_credentials(username, password):
    if username == admin_username and password == admin_password:
            admin_menu()
    if username in user_accounts.keys() and password == user_accounts[username]['password']:
        print('Log in Successful..')
        logged_in_menu(username)
    else:
        print("Wrong Username or Password. Please Try again..")
    
# Main function to run the program
def main():
    print('Welcome!')
    while True:
        print('============================')
        print('[1] Register\n[2] Log in')
        try:
            choice = int(input('Enter [1 or 2]: '))
        except Exception:
            print("Incorrect input. Please try again.")
            continue
        if choice == 1:
            register_user()
        elif choice == 2:
            while True:
                username = input("Username(leave blank to return): ")
                if username == "":
                    break
                password = input("Password: ")
                check_credentials(username, password)
                break
        else:
            print("Incorrect input. Please try again.")

if __name__ == "__main__":  
    main()
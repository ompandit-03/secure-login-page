import getpass

from password_hashing import hash_function,verify

from file_handling import save_data,load_data

users , locked_users = load_data()

def main():
    while True:

        print("""
        ===================
        SECURE LOGIN SYSTEM
        ===================
        """)

        print("""
            1.Register
            2.Login
            3.Exit
        """)
        try:
            user_choice = int(input("Enter the initals(1,2,3) of it:\n"))
            print("Your choice is:",user_choice)
        except ValueError:
            print("Invalid input! Please enter 1, 2, or 3.")
            continue

        if user_choice == 1:
            print("You selected 1.Register")
            username = input("enter your username:\n")

            if not username.strip():
                print("username cannot be empty.")
                continue

            if username in users:
                print("username already exist")
            else:
                password = getpass.getpass("create your password:\n")
                if not password.strip():
                    print("password cannot be empty")
                    continue

                salt , password_hash = hash_function(password)
    
                users[username] = (salt , password_hash)
                print("registration successful")
                save_data(users,locked_users)
                
        elif user_choice == 2:
            print("You selected 2.Login")

            username = input("Enter Your Username:\n")
            
            if not username.strip():
                print("username cannot be empty.")
                continue

            if username in locked_users:
                print("Your account is locked, Login denied.")     
                
            elif username in users:
                remaining_attempts = 3
                salt , password_hash = users.get(username)
                
                while remaining_attempts > 0:
                    print("Remaining Attempts: ", remaining_attempts)
                    password = getpass.getpass("Enter your Password:\n")
                    
                    storedpassword = verify(password,salt,password_hash)
                    
                    if storedpassword:
                        print("access granted, Login Successful")
                        break
                    else:
                        remaining_attempts -=1
                        print("Incorrect Password")

                if remaining_attempts == 0:
                    locked_users.add(username)
                    print("Too many Attempts, you are locked out")
                    save_data( users , locked_users)
            else:
                print("User not found, Register the user")

        elif user_choice == 3:
            print("You selected 3.Exit")
            break
        else:
            print("choose right number")

if __name__=="__main__":
    main()


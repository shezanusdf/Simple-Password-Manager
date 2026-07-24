import json
passwords = {}
def main():
    while True:
        print(
'''
==============
PASSWORD VAULT
==============
1. Add 
2. View
3. Delete
4. Exit
Enter your choice(1-4)''')
        choice = int(input("> "))
        if choice == 1:
            add_password()
            continue
        elif choice == 2:
            view_password()
            continue
        elif choice == 3:
            delete_password()
            continue
        elif choice == 4:
            break
        
def add_password():
    global passwords
    website = input("Enter Website Name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords[website] = {
        "username" : username,
        "password" : password
    }
    with open("records.json","a") as file:
        json.dump(passwords, file, indent = 4)
    
def view_password():
    global passwords
    website = input("Enter Website Name: ")
    with open("records.json","r") as file:
        passwords = json.load(file)
    for website, details in passwords.items():
        print(f"Website : {website}")
        print(f"username : {details["username"]}")
        print(f"Password : {details["password"]}")

def delete_password():
    pass

if __name__ == "__main__":
    main()
import json

def main():
    while True:
        print(
'''
==============
PASSWORD VAULT
==============
1. Add 
2. View
3. Edit
4. Delete
5. Exit
Enter your choice(1-5)''')
        choice = int(input("> "))
        passwords = load_records()
        if choice == 5:
            break
        website = input("Enter Website Name: ")
        if choice == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            add_password(passwords, website, username, password)
            continue
        elif choice == 2:
            view_password(passwords, website)
            continue
        elif choice == 3:
            edit_password(passwords, website)
            continue
        elif choice == 4:
            delete_password(passwords, website)
            continue

def take_input():
    website = input("> ")
    return website

def load_records():
    with open("records.json","r") as file:
        try:
            return json.load(file)
        except:
            return {}
    
def dump_records(passwords):
    with open("records.json","w") as file:
        json.dump(passwords, file, indent = 4)

def add_password(passwords, website, username, password):
    passwords[website] = {
        "username" : username,
        "password" : password
    }
    dump_records(passwords)
        
    
def view_password(passwords, website):
    for websites, details in passwords.items():
        if website == websites:
            print(f"Website : {websites}")
            print(f"username : {details["username"]}")
            print(f"Password : {details["password"]}")

def edit_password(passwords, website):
    if website in passwords:
        print("Enter New Password.")
        new_password = input("> ")
        passwords[website]["password"] = new_password
        dump_records(passwords)
        print("Record successfully changed!")
    else:
        print("Record does not exist!")

def delete_password(passwords, website):
    if website in passwords:
        del(passwords[website])
        dump_records(passwords)
        print("Record successfully deleted!")
    else:
        print("Record does not exist!")

if __name__ == "__main__":
    main()
import storage
import vault

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
    try:
        choice = int(input("> "))
        if choice not in range(1,6):
            print("Enter valid choice!")
            continue
    except:
        print("Enter valid choice!")
        continue
    passwords = storage.load_records()
    if choice == 5:
        break
    website = input("Enter Website Name: ")
    if choice == 1:
        username = input("Enter Username: ")  
        password = input("Enter Password: ")
        vault.add_password(passwords, website, username, password)
        continue
    elif choice == 2:
        vault.view_password(passwords, website)
        continue
    elif choice == 3:
        vault.edit_password(passwords, website)
        continue
    elif choice == 4:
        vault.delete_password(passwords, website)
        continue


from storage import dump_records
def add_password(passwords, website, username, password):
    if website not in passwords:
        passwords[website] = {
            "username" : username,
            "password" : password
        }
        dump_records(passwords)
    else:
        print("Record already exists!")
        
    
def view_password(passwords, website):
    if website in passwords:
        print(f"Website : {website}")
        print(f"username : {passwords[website]["username"]}")
        print(f"Password : {passwords[website]["password"]}")
    else:
        print("Record doesnt exist!")

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
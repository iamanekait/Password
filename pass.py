import csv
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(platform, password):
    with open('passwords.csv', 'a', newline='') as csvfile:
        fieldnames = ['Platform', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({'Platform': platform, 'Password': password})

def update_password(platform, new_password):
    passwords = []
    with open('passwords.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Platform'] == platform:
                row['Password'] = new_password
            passwords.append(row)
    
    with open('passwords.csv', 'w', newline='') as csvfile:
        fieldnames = ['Platform', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(passwords)

def delete_password(platform):
    passwords = []
    with open('passwords.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Platform'] != platform:
                passwords.append(row)
    
    with open('passwords.csv', 'w', newline='') as csvfile:
        fieldnames = ['Platform', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(passwords)

def main():
    print("Welcome to the Password Manager!")
    choice = input("Would you like to (C)reate, (U)pdate, or (D)elete a password? (Press any other key to exit): ").upper()
    
    if choice == 'C':
        platform = input("Please enter the platform you are going to use the password for: ")
        length = int(input("Please enter the desired length of the password: "))
        password = generate_password(length)
        print(f"\nYour generated password for {platform} is: {password}\n")
        save_password(platform, password)
    elif choice == 'U':
        platform = input("Please enter the platform you want to update the password for: ")
        option = input("Would you like to (G)enerate a new password or (E)nter one yourself? ").upper()
        if option == 'G':
            length = int(input("Please enter the desired length of the password: "))
            new_password = generate_password(length)
            print(f"\nYour generated password for {platform} is: {new_password}\n")
            update_password(platform, new_password)
            print("Password updated successfully!")
        elif option == 'E':
            new_password = input("Please enter the new password: ")
            update_password(platform, new_password)
            print("Password updated successfully!")
        else:
            print("Invalid option!")
    elif choice == 'D':
        platform = input("Please enter the platform you want to delete the password for: ")
        delete_password(platform)
        print("Password deleted successfully!")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()

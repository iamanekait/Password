# Password Manager

This simple Python script serves as a basic password manager. It allows users to create, update, or delete passwords for different platforms.

## Prerequisites

Before using this script, make sure you have Python installed on your system. This script utilizes the `csv`, `random`, and `string` modules, which are typically included in standard Python installations.

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/password-manager.git
   ```

2. **Navigate to the Directory**: Enter the directory containing the `password_manager.py` file.

   ```bash
   cd password-manager
   ```

3. **Run the Script**: Execute the script by running the following command:

   ```bash
   python password_manager.py
   ```

4. **Follow the Prompts**: The script will prompt you with options to create, update, or delete a password.

## Functions

- **generate_password(length)**: Generates a random password of the specified length.
- **save_password(platform, password)**: Saves the password for a given platform to a CSV file.
- **update_password(platform, new_password)**: Updates the password for a specified platform in the CSV file.
- **delete_password(platform)**: Deletes the password entry for a given platform from the CSV file.

## Usage

- **Create a Password**: Choose the 'C' option, enter the platform, and specify the desired length for the password. A randomly generated password will be displayed and saved.
- **Update a Password**: Choose the 'U' option, enter the platform for which you want to update the password. You can choose to generate a new password or enter one manually.
- **Delete a Password**: Choose the 'D' option, enter the platform for which you want to delete the password.

## Note

- Passwords are stored in a CSV file named `passwords.csv` in the same directory as the script.
- Always ensure the security of your CSV file and avoid sharing it with unauthorized individuals.

## Author

This script was created by [Your Name]. Feel free to contact me with any questions or suggestions!
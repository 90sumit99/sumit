import secrets
import string

def generate_password(website_name, logo_name, length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    # Include the logo name in the password
    password = f"{logo_name}_{password}"

    return password

# Example usage:
website_name = input("Enter the website name: ")
logo_name = input("Enter the logo name: ")
password = generate_password(website_name, logo_name)
print(f"Generated password for {website_name} with logo {logo_name}: {password}")

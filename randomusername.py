import random
import string

adjectives = ["Cool", "Fast", "Brave", "Happy", "Dark", "Mighty", "Clever", "Silent"]
nouns = ["Tiger", "Eagle", "Ninja", "Warrior", "Panther", "Shadow", "Knight", "Dragon"]

def generate_username(include_number=True, include_special_char=False):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    username = adj + noun

    if include_number:
        username += str(random.randint(10, 99))

    if include_special_char:
        username += random.choice(string.punctuation)

    return username


def save_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")


if __name__ == "__main__":
    print("Welcome to the Random Username Generator!")

    include_number = input("Include numbers in the username? (yes/no): ").strip().lower() == "yes"
    include_special_char = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    generated_username = generate_username(include_number, include_special_char)

    print(f"Generated Username: {generated_username}")

    save_to_file(generated_username)
    print("Username saved to usernames.txt!")
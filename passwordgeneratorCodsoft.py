import string
import random
import secrets

def get_char_pool(style):
    if style == 'sci-fi':
        return string.ascii_letters + string.digits + "!@#*^&"
    elif style == 'fantasy':
        return "aeiou" + "".join(secrets.choice(["dr", "or", "th", "el", "an"])) + string.digits + "!*"
    elif style == 'gamer':
        return "n00bL3v3lUp!" + string.digits
    elif style == 'emoji':
        return string.ascii_letters + string.digits + "🤖🔥💥🛡️🧠🚀💣"
    elif style == 'minimalist':
        return string.ascii_lowercase + string.digits
    else:
        return string.ascii_letters + string.digits + string.punctuation

def generate_password(length=12, style="default"):
    pool = get_char_pool(style)
    if len(pool) == 0:
        print("Invalid character pool.")
        return ""
    return ''.join(secrets.choice(pool) for _ in range(length))

# Example usage:
print("Choose a password style: sci-fi, fantasy, gamer, emoji, minimalist")
style = input("Enter style: ").lower()
length = int(input("Enter password length: "))
password = generate_password(length, style)
print(f"Here's your {style}-style password: {password}")

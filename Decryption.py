import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.seed(10)
random.shuffle(key)
cipher_text = input("Enter a message to decrypt:")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message : {cipher_text}")
print(f"original message : {plain_text}")

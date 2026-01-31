import random
import string

print("!!Encryption And Decryption")

x = int(input("Enter 1 for Encryption and 2 for Decryption"))
k = 3
if x < 1 or x > 2:
    raise ValueError("Rerun the program")
elif x == 1:
    encrypt = []
    a = input("Enter the word or sentence to encrypt")
    encrypt.append(a)
    b = encrypt[0][::-1]
    rand_letters = "".join(random.choices(string.ascii_lowercase, k=k))
    encrypted_text = rand_letters + b + rand_letters[::-1]
    encrypt.append(encrypted_text)
    print(f"This is your encrypted text:{encrypt[1]}")
else:
    decrypt = []
    q = input("Enter the encrypted text: ")
    decrypt.append(q)

    encrypted_words = q.split()
    decrypted_words = []

    for word in encrypted_words:
        without_rand = word[k:-k]

        decrypted_word = without_rand[::-1]
        decrypted_words.append(decrypted_word)

    decrypted_text = " ".join(decrypted_words)
    decrypt.append(decrypted_text)
    print(f"Decrypted text: {decrypt[1]}")

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    plaintext = "Vigenère cipher  is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution. "
    key = 'LION'
    ciphertext = encryptMessage(key, plaintext)
    print(ciphertext)
    print()


def encryptMessage(key, plaintext):
    ciphertext = []
    keyIndex = 0
    key = key.upper()

    for letter in plaintext:
        num = LETTERS.find(letter.upper())
        if num != -1:
            num += LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if letter.isupper():
                ciphertext.append(LETTERS[num])
            elif letter.islower():
                ciphertext.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            ciphertext.append(letter)

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()

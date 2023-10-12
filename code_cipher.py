def caesar_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 1  # Shift value for Caesar Cipher
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result

# Example usage
text = input("Enter here: ")
encrypted_text = caesar_cipher(text)
print("Encrypted text:", encrypted_text)

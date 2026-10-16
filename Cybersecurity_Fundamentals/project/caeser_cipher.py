def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_key = int(input("Enter shift value: "))
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    
    output = caesar_cipher(message, shift_key, mode)
    print(f"Result: {output}")
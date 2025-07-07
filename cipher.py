def cipher(message, deslocation):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_message = ''

    for iLetter in range(len(message)):
        char = message[iLetter].lower()

        if (char not in alphabet):
            return ValueError(f'{char} not allowed')
        
        if char == ' ':
            ciphered_message += ' '
            continue

        deslocation_index = alphabet.index(char) + deslocation

        if deslocation_index > 25:
            deslocation_index -= 25
        
        ciphered_message += alphabet[deslocation_index]

    return ciphered_message

print(cipher('hello world', 3))

def cipher(message, deslocation):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_message = ''

    for iLetter in range(len(message)):
        char = message[iLetter].lower()

        if deslocation > 26:
            return ValueError('deslocation can only be lower or equal to 26')

        if char == ' ':
            ciphered_message += ' '
            continue

        if (char not in alphabet):
            return ValueError(f'{char} not allowed')

        deslocation_index = alphabet.index(char) + deslocation

        if deslocation_index > 25:
            deslocation_index -= 25
        
        ciphered_message += alphabet[deslocation_index]

    return ciphered_message

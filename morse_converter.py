# 1. The Translation Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Automatically create a reverse dictionary for decoding (Morse to Text)
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# 2. Encoding Function (Text to Morse)
def text_to_morse(text):
    morse_translated = []
    # Convert input to uppercase to match our dictionary keys
    text = text.upper()
    
    for char in text:
        if char == ' ':
            # Use 3 spaces to represent a gap between words
            morse_translated.append('   ')
        elif char in MORSE_CODE_DICT:
            # Add the morse code and a single space after each letter
            morse_translated.append(MORSE_CODE_DICT[char] + ' ')
        else:
            # If a character isn't in our dictionary, ignore or flag it
            print(f"Warning: Character '{char}' not supported.")
            
    # Join the list into a single string
    return ''.join(morse_translated)

# 3. Decoding Function (Morse to Text)
def morse_to_text(morse_code):
    text_translated = []
    # Split the morse code by the 3 spaces we used for word gaps
    words = morse_code.split('   ')
    
    for word in words:
        # Split each word by single spaces to get individual letters
        letters = word.split(' ')
        for letter in letters:
            if letter in REVERSE_DICT:
                text_translated.append(REVERSE_DICT[letter])
        # Add a space after each completed word
        text_translated.append(' ')
        
    # Join everything and strip off any trailing spaces
    return ''.join(text_translated).strip()

# 4. The User Interface (Terminal Loop)
def main():
    print("=== Morse Code Converter ===")
    while True:
        print("\nOptions:")
        print("1. Convert Text to Morse")
        print("2. Convert Morse to Text")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            user_text = input("Enter text to convert: ")
            result = text_to_morse(user_text)
            print(f"\nResult: {result}")
            
        elif choice == '2':
            user_morse = input("Enter Morse code (use 1 space between letters, 3 spaces between words): ")
            result = morse_to_text(user_morse)
            print(f"\nResult: {result}")
            
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# This ensures the menu only runs if this file is executed directly
if __name__ == '__main__':
    main()
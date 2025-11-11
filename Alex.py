import speech_recognition as sr #allows the program to convert spoken language into text.
import pyttsx3 #which is used to convert text to speech.
import pygame #used to play sound effects
import pyaudio

listener= sr.Recognizer() #This creates an instance of the Recognizer class from the speech_recognition library, which will be used to recognize speech.
engine = pyttsx3.init() #This initializes the text-to-speech engine.
voices = engine.getProperty('voices') #This gets the available voices for the text-to-speech engine.
selected_voice = None #This initializes a variable to store the selected voice.

for voice in voices: #This loop goes through each available voice and selects the first one that has "male" in its name.
    if "male" in voice.name.lower():
        selected_voice = voice
        break

if selected_voice is not None: #If a male voice was found, it sets the text-to-speech engine to use that voice.
    engine.setProperty('voice', selected_voice.id)

pygame.mixer.init() #This initializes the Pygame mixer, which handles sound playback.
sound_effect = pygame.mixer.Sound('activation.wav') #This loads a sound file (activation.wav) to be played later.

def talk(text): #This function takes text as input, converts it to speech, and waits until the speech is finished.
    engine.say(text)
    engine.runAndWait()

def play_waiting_sound(): #This function plays the sound effect loaded earlier.
    sound_effect.play()

def take_command(): #This function listens for a voice command, processes it, and returns the command as text.
    try:
        with sr.Microphone() as source:
            print('Alex: Say something...')
            play_waiting_sound()
            listener.adjust_for_ambient_noise(source)
            listener.pause_threshold = 1
            voice = listener.listen(source, timeout=20)
            command = listener.recognize_google(voice).lower()
            if 'alex' in command: #If the keyword "Alex" is detected in the command, it replaces it with "User:".
                command = command.replace('alex', 'User:')
            else: #If something goes wrong, it returns "try again".
                return "try again"
            return command
    except:
        return "try again"

#This prints and speaks a greeting message.
print('Hello! What can I help you with today? '
      'You can ask me to encrypt and decrypt words using ciphers. '
      'For ciphers, say "Alex, what is the encrypted/decrypted word of [your word] using '
      'Cipher A, Cipher B, Cipher C, or Cipher D," where Cipher A is Caesar, '
      'Cipher B is Atbash, Cipher C is Rot13, and Cipher D is Affine.')
talk('Hello!')

def caesar_cipher(text, shift, decrypt=False): #This function performs Caesar cipher encryption/decryption on the input text.
    if decrypt:
        shift = -shift
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def atbash_cipher(text): #This function performs Atbash cipher encryption on the input text.
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr(shift_amount + 25 - (ord(char) - shift_amount))
        else:
            encrypted_text += char
    return encrypted_text

def rot13_cipher(text): #This function performs ROT13 cipher encryption on the input text using the Caesar cipher function with a fixed shift of 13.
    return caesar_cipher(text, 13)

def affine_cipher(text, a, b, decrypt=False):
    """
    This function performs Affine cipher encryption or decryption on the input text.
    :param text: The text to be encrypted or decrypted.
    :param a: The multiplier key for the cipher. Must be coprime with 26 (the length of the alphabet).
    :param b: The shift key for the cipher. It can be any integer.
    :param decrypt: A boolean flag indicating whether to encrypt (False) or decrypt (True) the text.
    """

    # This helper function finds the modular inverse of 'a' with respect to 'm' (which is 26 in our case)
    # The modular inverse is a number that, when multiplied by 'a' and then taken the remainder when divided by 'm', gives 1
    def mod_inverse(a, m):
        a = a % m  # Ensure 'a' is within the range of 0 to m-1
        for x in range(1, m):
            if (a * x) % m == 1:  # Check if 'x' is the modular inverse of 'a'
                return x  # Return 'x' if it is the modular inverse
        return 1  # Return 1 if no modular inverse is found (although in practice 'a' should always have an inverse)

    # Initialize an empty string to store the encrypted/decrypted text
    encrypted_text = ''

    # If we're decrypting, calculate the modular inverse of 'a' (using the mod_inverse function)
    # Otherwise, just use the value of 'a' as it is
    a_inv = mod_inverse(a, 26) if decrypt else a

    # Loop through each character in the text
    for char in text:
        # If the character is an alphabetic character (a letter)
        if char.isalpha():
            # Determine the shift amount based on whether the character is uppercase or lowercase
            # Uppercase letters start at ASCII value 65, lowercase letters start at ASCII value 97
            shift_amount = 65 if char.isupper() else 97

            # If we're decrypting
            if decrypt:
                # Apply the decryption formula using the modular inverse of 'a' and subtracting 'b'
                # Convert the character to its numeric equivalent, apply the formula, and convert it back to a character
                encrypted_text += chr((a_inv * ((ord(char) - shift_amount - b) % 26)) % 26 + shift_amount)
            # If we're encrypting
            else:
                # Apply the encryption formula using 'a' and adding 'b'
                # Convert the character to its numeric equivalent, apply the formula, and convert it back to a character
                encrypted_text += chr((a * (ord(char) - shift_amount) + b) % 26 + shift_amount)

        # If the character is not an alphabetic character (e.g., punctuation, space, etc.)
        else:
            # Add the character to the encrypted_text string without any modification
            encrypted_text += char

    # Return the encrypted/decrypted text
    return encrypted_text

def spell_out(text): #This function spells out the text by separating each character with a space.
    return ' '.join(text)

def run_alex(): #This function listens for a command, processes it, and performs the appropriate action. It handles encryption and decryption requests using different ciphers.
    command = take_command()
    print(command)
    if command == "try again":
        return
    elif 'turn off' in command:
        talk("Thank you!")
        quit()
    elif 'encrypted word of' in command:
        try:
            text = command.split('encrypted word of')[1].split('using')[0].strip()
            cipher_number = command.split('using')[1].strip()
            if cipher_number == 'cipher a':
                encrypted_word = caesar_cipher(text, 3)  # Shift of 3 for Caesar cipher
                method = 'Caesar'
            elif cipher_number == 'cipher b':
                encrypted_word = atbash_cipher(text)
                method = 'Atbash'
            elif cipher_number == 'cipher c':
                encrypted_word = rot13_cipher(text)
                method = 'Rot13'
            elif cipher_number == 'cipher d':
                encrypted_word = affine_cipher(text, 5, 8)  # Example constants a=5, b=8 for Affine cipher
                method = 'Affine'
            else:
                talk("I beg your pardon?")
                return
            spelled_out = spell_out(encrypted_word)
            result = f'The encrypted word using {method} is - {spelled_out}'
            print(result)
            talk(result)

        except:
            talk("I beg your pardon?")
    elif 'decrypted word of' in command:
        try:
            text = command.split('decrypted word of')[1].split('using')[0].strip()
            cipher_number = command.split('using')[1].strip()
            if cipher_number == 'cipher a':
                decrypted_word = caesar_cipher(text, 3, decrypt=True)
                method = 'Caesar'
            elif cipher_number == 'cipher b':
                decrypted_word = atbash_cipher(text)
                method = 'Atbash'
            elif cipher_number == 'cipher c':
                decrypted_word = rot13_cipher(text)
                method = 'Rot13'
            elif cipher_number == 'cipher d':
                decrypted_word = affine_cipher(text, 5, 8, decrypt=True)
                method = 'Affine'
            else:
                talk("I beg your pardon?")
                return
            spelled_out = spell_out(decrypted_word)
            result = f'The decrypted word using {method} is - {spelled_out}'
            print(result)
            talk(result)

        except:
            talk("I beg your pardon?")
    else:
        talk("I beg your pardon?")

while True:
    run_alex() #This starts an infinite loop that keeps running the run_alex() function, continuously listening for and responding to commands.


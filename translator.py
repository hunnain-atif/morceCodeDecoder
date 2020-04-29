import re


def getUserInput():
    text = input("input text to translate... ")
    if (re.search(r'\d', text)):
        print('invlaid input, please try again')
        getUserInput()
    else: 
        translatedText = translate(text)
        print(translatedText)

def translate(textToTranslate):

    #creates dictionary for encoding english letters to morse code
    encodingDictionary = {
    'A': '.-', 'B':'-...', 'C': '-.-.',
    'D': '-..', 'E':'.',   'F': '..-.',
    'G': '--.', 'H':'....', 'I': '..',
    'J': '.---', 'K':'-.-', 'L': '.-..',
    'M': '--', 'N':'-.', 'O': '---',
    'P': '.--.', 'Q':'--.-', 'R': '.-.',
    'S': '...', 'T':'-', 'U': '..-',
    'V': '...-', 'W':'.--', 'X': '-..-',
    'Y': '-.--', 'Z':'--..', ' ': '/',
    }

    #creates an inverse dictionary to above for decoding morse code to english letters
    decodingDictionary = {value: key for key,value in encodingDictionary.items()}

    #check to see if text is morse code
    if re.match('(\s|-|\.)+', textToTranslate):
        #decrypt each morse code letter using dictionary and place in string
        return ''.join(decodingDictionary[letter] for letter in textToTranslate.split())
    else:
        return ' '.join(encodingDictionary[letter] for letter in textToTranslate.upper())

if __name__ == "__main__":
    getUserInput()


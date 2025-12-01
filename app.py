# Import libraries from the flask framework
from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)

# Morse code dictionary with the letters and numbers
# a space would be "/"
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

# This function converts the text the user inputs into morse code
def text_to_morse(text):
    # empty morse code list to store the morse code characters
    morse = []
    # iterating through the characters that the user will input
    for char in text.upper():
        # if the character is in the morse code dictionary
        if char in MORSE_CODE:
            # then append it to the empty morse code list, after looking it up in the
            # dictionary and getting the index (the morse code)
            morse.append(MORSE_CODE[char])
    # join method is when you take all the items in the iterables and join them into one string
    return ' '.join(morse)

# GET is loading the page, POST is submitting the form request
@app.route('/', methods=['GET', 'POST'])
# Define the main route of the web page
def index():
    # stores the morse code output, None since there is no input yet
    result = None
    # stores what the user wants to type
    input_text = ''
    # check if the user submitted the form
    if request.method == 'POST':
        # get the text the user entered in 
        # '' if the user didn't enter in anything 
        input_text = request.form.get('input_text', '')
        # translate the users text to morse code
        result = text_to_morse(input_text)
    # render the HTML template, then displaying the values 
    return render_template('index.html', result=result, input_text=input_text)
# start the development server
if __name__ == '__main__':
    # debug is true when reloaded to show error messages
    app.run(debug=True)
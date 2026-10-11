from flask import Flask, render_template, request, jsonify
from morse_converter import text_to_morse, morse_to_text

app = Flask(__name__)

# Route 1: The new Welcome/Intro page
@app.route('/')
def home():
    return render_template('intro.html')

# Route 2: The actual Converter tool
@app.route('/converter')
def converter():
    return render_template('converter.html')

# Route 3: The API Endpoint that handles the conversion
@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    input_text = data.get('text', '')
    mode = data.get('mode', 'text_to_morse')
    
    if mode == 'text_to_morse':
        result = text_to_morse(input_text)
    elif mode == 'morse_to_text':
        result = morse_to_text(input_text)
    else:
        result = "Invalid mode selected."
        
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
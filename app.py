from flask import Flask, render_template, request, jsonify
# Import the functions you wrote in Step 1!
from morse_converter import text_to_morse, morse_to_text

app = Flask(__name__)

# Route 1: Serve the frontend website
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: The API Endpoint that handles the conversion
@app.route('/convert', methods=['POST'])
def convert():
    # Extract the data sent by the frontend
    data = request.get_json()
    input_text = data.get('text', '')
    mode = data.get('mode', 'text_to_morse')
    
    # Process the data using your Step 1 engine
    if mode == 'text_to_morse':
        result = text_to_morse(input_text)
    elif mode == 'morse_to_text':
        result = morse_to_text(input_text)
    else:
        result = "Invalid mode selected."
        
    # Send the result back to the frontend in JSON format
    return jsonify({'result': result})

if __name__ == '__main__':
    # Run the server in debug mode so it updates when you save changes
    app.run(debug=True)
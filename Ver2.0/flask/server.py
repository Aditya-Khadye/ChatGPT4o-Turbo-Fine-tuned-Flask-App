"""
Project: Finetuned AI Assistant
Author: Aditya Khadye
Date: 2025-01-22

Description:
This script is part of the Finetuned AI Assistant project. It provides backend functionality for the chatbot, 
including generating AI responses, saving chat history, and retrieving stored conversations.

Technologies used:
- Flask: For routing and backend APIs.
- Flask-CORS: For handling cross-origin requests.
- Flask-SQLAlchemy: For SQLite database integration.
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database model for chat history
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=False)  # User input
    response = db.Column(db.Text, nullable=False)  # AI-generated response

# Ensure all database tables are created
db.create_all()

# Load training data from a JSONL file
def load_training_data():
    with open('trainingData.jsonl', 'r') as file:
        return [json.loads(line) for line in file]

training_data = load_training_data()

# Serve the main HTML interface
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to handle user prompts and return AI responses
@app.route('/get-chatgpt-response', methods=['POST'])
def get_chatgpt_response():
    data = request.json
    prompt = data.get('prompt', '')

    # Generate a mock response or look up training data
    response = f"Mock response for: {prompt}"
    for item in training_data:
        if prompt.lower() in item['prompt'].lower():
            response = item['completion']
            break

    return jsonify({'response': response})

# Endpoint to save chat history to the database
@app.route('/save-chat', methods=['POST'])
def save_chat():
    data = request.json
    prompt = data.get('prompt')
    response = data.get('response')

    if prompt and response:
        chat = ChatHistory(prompt=prompt, response=response)
        db.session.add(chat)
        db.session.commit()
        return jsonify({'message': 'Chat saved successfully'}), 201

    return jsonify({'error': 'Invalid data'}), 400

# Endpoint to retrieve chat history from the database
@app.route('/history', methods=['GET'])
def get_history():
    chats = ChatHistory.query.all()
    history = [{'prompt': chat.prompt, 'response': chat.response} for chat in chats]
    return jsonify(history)

if __name__ == '__main__':
    # Run the Flask app on port 5500 with debugging enabled
    app.run(debug=True, port=5500)